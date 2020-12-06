from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShortenerConfig(AppConfig):
    name = 'shortit.shortener'
    verbose_name = _("Shortener")

    def ready(self):
        try:
            import shortit.shortener.signals  # noqa F401
        except ImportError:
            pass
