from django.http import HttpResponseRedirect
from django.shortcuts import  get_object_or_404

from django.views import View
from shortit.shortener.models import ShortUrl
from shortit.analytics.models import ClickEvent


class ShortUrlRedirectView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        """
        handles the redirection of the urls
        """
        obj = get_object_or_404(ShortUrl, shortcode=shortcode)
        click_obj = ClickEvent.objects.create_event(obj)
        print(click_obj)
        return HttpResponseRedirect(obj.url)
