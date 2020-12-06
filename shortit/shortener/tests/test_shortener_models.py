import pytest
from django.conf import settings
from shortit.shortener.models import ShortUrl

pytestmark = pytest.mark.django_db

SHORT_PREFIX = getattr(settings, "SHORT_PREFIX", "tier.app")

def test_get_short_url(url: ShortUrl):
    assert url.get_short_url() == f"http://localhost:8000/{SHORT_PREFIX}{url.shortcode}/"
