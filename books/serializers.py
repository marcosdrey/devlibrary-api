from rest_framework import serializers
from django.db.models import Avg, Count
from .models import Book, BookReview
from genres.models import Genre
from subgenres.models import Subgenre
from themes.models import Theme
from genres.serializers import GenreIDNameSerializer
from subgenres.serializers import SubgenreIDNameSerializer
from publishers.serializers import PublisherSerializer
from authors.serializers import AuthorGETSerializer
from themes.serializers import ThemeSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_photo(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError("O tamanho do arquivo deve ser menor do que 1MB.")
        return value

    def validate_subgenre(self, value):
        genre_id = self.initial_data.get('genre')
        if genre_id:
            try:
                genre = Genre.objects.get(id=genre_id)
                allowed_subgenres = genre.subgenres.all()
                subgenre = Subgenre.objects.get(name=value)
                if subgenre not in allowed_subgenres:
                    raise serializers.ValidationError(f'{subgenre} não é válido para o gênero {genre}.')
            except Genre.DoesNotExist:
                raise serializers.ValidationError('O gênero especificado não existe')
        return value

    def validate_themes(self, value):
        subgenre_id = self.initial_data.get('subgenre')
        if subgenre_id:
            try:
                subgenre = Subgenre.objects.get(id=subgenre_id)
                allowed_themes_ids = subgenre.themes.values_list('id', flat=True)
                themes_ids_prompted = [theme.id for theme in value]
                invalid_themes = [Theme.objects.get(id=theme_id) for theme_id in themes_ids_prompted if theme_id not in allowed_themes_ids]
                if invalid_themes:
                    raise serializers.ValidationError(f"Os seguintes temas não são válidos para o subgênero {subgenre}: "
                                                      f"{", ".join(map(str, invalid_themes))}")
            except Subgenre.DoesNotExist:
                raise serializers.ValidationError("O subgênero especificado não existe.")
        return value


class BookGETSerializer(serializers.ModelSerializer):
    stars = serializers.SerializerMethodField(read_only=True)
    genre = GenreIDNameSerializer()
    subgenre = SubgenreIDNameSerializer()
    publisher = PublisherSerializer()
    themes = ThemeSerializer(many=True)
    authors = AuthorGETSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'stars', 'genre',
                  'subgenre', 'themes', 'authors', 'publisher',
                  'release_date', 'photo', 'description')

    def get_stars(self, obj):
        stars = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        if stars:
            return round(stars, 1)
        return None


class BookGETReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = BookReview
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}


class BookReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookReview
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}


class BookReviewRelatedSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = BookReview
        fields = ('id', 'rating', 'comment', 'user', 'created_at', 'likes')

    def get_user(self, obj):
        user_info = {
            'id': obj.user.id,
            'name': obj.user.username
        }
        return user_info


class BookSingleGETSerializer(serializers.ModelSerializer):
    stars = serializers.SerializerMethodField(read_only=True)
    genre = GenreIDNameSerializer()
    subgenre = SubgenreIDNameSerializer()
    publisher = PublisherSerializer()
    themes = ThemeSerializer(many=True)
    authors = AuthorGETSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'stars', 'genre',
                  'subgenre', 'themes', 'authors', 'publisher',
                  'release_date', 'photo', 'description', 'reviews')

    def get_stars(self, obj):
        stars = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        if stars:
            return round(stars, 1)
        return None

    def get_reviews(self, obj):
        reviews = obj.reviews.all().annotate(order_likes=Count('likes')).order_by('-order_likes')
        return BookReviewRelatedSerializer(reviews, many=True).data


class BookReviewLikeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def validate(self, attrs):
        request_user = self.context.get('request').user
        user_id = attrs.get('user_id')

        if not user_id or request_user.id != user_id:
            raise serializers.ValidationError('ID de usuário não foi informado ou não é correspondente ao seu ID.')
        return attrs

    def update(self, instance, validated_data):
        user_id = validated_data.get('user_id')
        review_id = self.context.get('view').kwargs.get('pk')
        try:
            review = BookReview.objects.get(id=review_id)
            review_likes_ids = review.likes.all().values_list('id', flat=True)
            user_already_liked = bool(user_id in review_likes_ids)
            if user_already_liked:
                review.likes.remove(user_id)
            else:
                review.likes.add(user_id)
            review.save()
            return review
        except BookReview.DoesNotExist:
            raise serializers.ValidationError('Essa review não existe. Tente novamente')

    def to_representation(self, instance):
        review_id = self.context.get('view').kwargs.get('pk')
        try:
            review = BookReview.objects.get(id=review_id)
            book = review.book
            return BookSingleGETSerializer(book).data
        except BookReview.DoesNotExist:
            raise serializers.ValidationError('Essa review não existe. Tente novamente')
