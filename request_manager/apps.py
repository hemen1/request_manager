from django.apps import AppConfig


class RequestManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'request_manager'

    def ready(self):
        import request_manager.signals