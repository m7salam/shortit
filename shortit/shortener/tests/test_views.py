# from django.http import request
# import pytest
# from django.contrib.auth.models import AnonymousUser
# from django.http.response import Http404, HttpResponse
# from django.shortcuts import get_object_or_404
# from django.test import RequestFactory

# from shortit.shortener.models import ShortUrl
# from shortit.shortener.views import short_url_redirect_view
# from shortit.shortener.tests.factories import UrlFactory

# pytestmark = pytest.mark.django_db



# class TestShortUrlRedirectVieww:
#     def test_get_redirect_url(self, short_url: ShortUrl, rf: RequestFactory):
        
#         request = rf.get("/fake-url")
#         view = short_url_redirect_view(request)
#         obj = get_object_or_404(short_url, shortcode=shortcode)
#          = short_url

#         view.request = request

#         assert HttpResponse == f"{obj.url}/"


