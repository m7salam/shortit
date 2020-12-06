from rest_framework import serializers

from shortit.shortener.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['url', "shortcode"]
