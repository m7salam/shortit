from shortit.analytics.api.serializers import ClickEventSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

# from shortit.analytics.api.serializers import ClickEventSerializer
from shortit.analytics.models import ClickEvent
from shortit.shortener.models import ShortUrl


class CountHits(RetrieveAPIView):
    """
     returns the count of a certain url clicks
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):

        shortcode = self.request.GET.get('q')
        print(shortcode)
        click_qs = ClickEvent.objects.filter(short_url__shortcode=shortcode)
        if click_qs.exists():
            click_event = click_qs.first()
            click_count = click_event.count
            print(click_count)
            data = {"count": click_count}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({'status': 'no short url found'}, status=status.HTTP_404_NOT_FOUND)

        # full_url = f"{request.build_absolute_uri('/')}{obj.shortcode}/"
