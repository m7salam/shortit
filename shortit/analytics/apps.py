from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AnalyticsConfig(AppConfig):
    name = 'shortit.analytics'
    verbose_name = _("Analytics")

    def ready(self):
        try:
            import shortit.analytics.signals  # noqa F401
        except ImportError:
            pass



