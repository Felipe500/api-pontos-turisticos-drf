from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    name = 'app.reviews'

    def ready(self) -> None:
        from . import signals  # noqa: F401
