from django.apps import AppConfig


class ParentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parent'

    def ready(self) -> None:
        from . import signals
        return super().ready()