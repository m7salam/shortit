from typing import SupportsRound
from rest_framework import serializers

from shortit.analytics.models import ClickEvent


class ClickEventSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(source="short_url.shortcode")

    class Meta:
        model = ClickEvent
        fields = ['id', 'short_url', "count"]
