
from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    name = 'feedback'
    verbose_name = "Обратная связь"

    def ready(self):
        import feedback.signals
