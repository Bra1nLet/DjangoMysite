from django.apps import AppConfig


class CatsConfig(AppConfig):
    default_cats_field = 'django.db.models.BigAutoField'
    name = 'cats'
