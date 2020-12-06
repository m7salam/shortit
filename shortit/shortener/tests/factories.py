from typing import Any, Sequence

from factory import Faker
from factory.django import DjangoModelFactory
from shortit.shortener.models import ShortUrl

class UrlFactory(DjangoModelFactory):

    url = Faker("url")


    class Meta:
        model = ShortUrl
        django_get_or_create = ["url"]
