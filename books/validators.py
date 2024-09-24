from django.core.validators import BaseValidator


class MaxDateValidator(BaseValidator):

    def compare(self, date, limit_date):
        return date > limit_date
