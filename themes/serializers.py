from rest_framework import serializers
from .models import Theme


class ThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'

    def validate_name(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('O tema não pode conter mais de 100 caracteres.')
        return value
