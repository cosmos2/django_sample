from django_extensions.db.models import TimeStampedModel
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel


__all__ = ("DefaultModel",)


class DefaultModel(SafeDeleteModel, TimeStampedModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    class Meta:
        abstract = True
