
from django.db import models
from django.urls import reverse
from django.conf import settings
from shortit.utils.code_generator import create_shortcode


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
SHORT_PREFIX = getattr(settings, "SHORT_PREFIX", "tier.app")

class ShortUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        """
        refresh all shortcodes to new ones
        """
        qs = ShortUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1

        return f"New codes made: {new_codes}"


class ShortUrl(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = ShortUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            #SHORT_PREFIX + 
            self.shortcode = create_shortcode(self)
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        # url_path = reverse("shortcode", shortcode=self.shortcode)
        return "http://localhost:8000" + reverse("shortcode", kwargs={"shortcode": self.shortcode})
