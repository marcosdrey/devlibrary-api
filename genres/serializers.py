from rest_framework import serializers
from .models import Genre
from subgenres.serializers import SubgenreGETSerializer


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

    def validate_name(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('O nome do gênero não pode conter mais de 100 caracteres.')
        return value


class GenreGETSerializer(serializers.ModelSerializer):
    subgenres = SubgenreGETSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'subgenres')


class GenreIDNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')
