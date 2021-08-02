from django.db import models
from django.conf import settings

from users.models import User
from utils.django.models import DefaultModel
from taggit.managers import TaggableManager


class Bookmark(DefaultModel):
    url = models.URLField("북마크 url", max_length=256)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="작성자",
        on_delete=models.CASCADE,
        related_name="bookmark_set",
        related_query_name="bookmark",
    )
    tags = TaggableManager(blank=True)

    class Meta:
        unique_together = ["url", "author"]

    def __str__(self):
        return f"[{self.id}] / {self.author}"
