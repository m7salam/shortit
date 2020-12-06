from django.conf.urls import url
from django.http import response
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shortit.shortener.api.serializers import ShortUrlSerializer

from shortit.shortener.models import ShortUrl


class CreateShortUrl(APIView):
    """
     Handles the response of the post request to the api which returns  the short url
    """
    parser_classes = [JSONParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ShortUrlSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        validated_data = serializer.validated_data
        qs = ShortUrl.objects.filter(url__iexact=validated_data.get("url"))

        if qs.exists():
            obj = qs.first()
            # full_url = f"{request.build_absolute_uri('/')}{obj.shortcode}/"
            data = {"short_url": obj.get_short_url(),
                    "shortcode": obj.shortcode}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
