from rest_framework import serializers
from themes.serializers import ThemeSerializer
from .models import Subgenre


class SubgenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subgenre
        fields = '__all__'


class SubgenreGETSerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True)

    class Meta:
        model = Subgenre
        fields = ('id', 'name', 'themes')


class SubgenreIDNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subgenre
        fields = ('id', 'name', 'icon')
