import random

from django.db import models, IntegrityError
from django.conf import settings


class Link(models.Model):
    full_link = models.URLField()
    shortened_link = models.CharField(max_length=30, unique=True)
    count_of_clicks = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            while True:
                self.shortened_link = self._create_shortened_link()
                try:
                    super().save(*args, **kwargs)
                    break
                except IntegrityError:
                    continue
        else:
            super().save(*args, **kwargs)

    def _create_shortened_link(self):
        shortened_link = ''.join(random.choices(settings.CHARACTERS, k=settings.LINK_LENGTH))
        return shortened_link

    def __str__(self):
        return f"{self.shortened_link} → {self.full_link}"
