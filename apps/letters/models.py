from django.db import models
from django.conf import settings

from users.models import User
from utils.django.models import DefaultModel


class Letter(DefaultModel):
    title = models.CharField("제목", max_length=24, blank=True, null=True)
    content = models.TextField("내용", blank=False, null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="작성자",
        on_delete=models.DO_NOTHING,
        related_name="letter_set",
        related_query_name="letter",
    )

    class Meta:
        unique_together = ["title", "content"]

    def __str__(self):
        return f"[{self.title}] / {self.author}"
