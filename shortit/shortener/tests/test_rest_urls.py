import pytest
from django.urls import resolve, reverse

from shortit.shortener.models import ShortUrl

pytestmark = pytest.mark.django_db


def test_shortit():
    assert reverse("api:shortener_api:shortit") == "/api/shortit/"
    assert resolve("/api/shortit/").view_name == "api:shortener_api:shortit"
