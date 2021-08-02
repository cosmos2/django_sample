from django_extensions.db.models import TimeStampedModel
from safedelete.models import SafeDeleteModel


__all__ = ("DefaultModel",)


class DefaultModel(SafeDeleteModel, TimeStampedModel):
    pass
