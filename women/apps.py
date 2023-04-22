from django.apps import AppConfig


class WomenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'women'
    verbose_name = 'Women of the world'  # Changing the category name in the admin panel
