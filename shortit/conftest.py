import pytest

from shortit.users.models import User
from shortit.shortener.models import ShortUrl
from shortit.users.tests.factories import UserFactory
from shortit.shortener.tests.factories import UrlFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def url() -> ShortUrl:
    return UrlFactory()
