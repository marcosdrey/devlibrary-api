from django.apps import AppConfig


class SubgenresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subgenres'

    def ready(self):
        import subgenres.signals
