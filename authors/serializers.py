from rest_framework import serializers
from .models import Author, Nationality


class NationalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Nationality
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class AuthorGETSerializer(serializers.ModelSerializer):
    nationality = NationalitySerializer()

    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality')
