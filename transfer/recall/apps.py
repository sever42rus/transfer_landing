from django.apps import AppConfig


class RecallConfig(AppConfig):
    name = 'recall'
    verbose_name = "Отзывы"

    def ready(self):
        import recall.signals
