from django.core.management.base import BaseCommand, CommandError
from shortit.shortener.models import ShortUrl


class Command(BaseCommand):
    help = 'Refreshes all the url shortcodes'


    def handle(self, *args, **options):
        return ShortUrl.objects.refresh_shortcodes()