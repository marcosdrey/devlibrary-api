from django.core.validators import BaseValidator


class MaxSizeValidator(BaseValidator):

    def clean(self, value):
        return value.size

    def compare(self, size, limit_size):
        return size > limit_size
