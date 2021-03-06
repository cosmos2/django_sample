from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet as DefaultGenericViewSet

__all__ = (
    "ViewSetMixin",
    "ListModelViewSet",
    "CreateModelViewSet",
    "RetrieveModelViewSet",
    "UpdateModelViewSet",
    "DestroyModelViewSet",
    "RetrieveUpdateModelViewSet",
    "RetrieveUpdateDestroyModelViewSet",
    "ReadOnlyModelViewSet",
    "ModelViewSet",
)


class GetSerializerClassMixin:
    serializer_classes = {}

    def get_serializer_class(self):
        try:
            action = getattr(self, "action")
            method = getattr(getattr(self, "request"), "method")

            if action:
                return self.serializer_classes[action]
            if method:
                return self.serializer_classes[self.request.method]
        except (KeyError, AttributeError):
            pass
        return super().get_serializer_class()


class ViewSetMixin(GetSerializerClassMixin):
    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs and isinstance(kwargs["data"], list):
            kwargs.setdefault("many", True)
        return super().get_serializer(*args, **kwargs)


class ListModelViewSet(ViewSetMixin, mixins.ListModelMixin, DefaultGenericViewSet):
    pass


class CreateModelViewSet(ViewSetMixin, mixins.CreateModelMixin, DefaultGenericViewSet):
    pass


class RetrieveModelViewSet(ViewSetMixin, mixins.RetrieveModelMixin, DefaultGenericViewSet):
    pass


class UpdateModelViewSet(ViewSetMixin, mixins.UpdateModelMixin, DefaultGenericViewSet):
    pass


class DestroyModelViewSet(ViewSetMixin, mixins.DestroyModelMixin, DefaultGenericViewSet):
    pass


class RetrieveUpdateModelViewSet(
    ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    DefaultGenericViewSet,
):
    pass


class RetrieveUpdateDestroyModelViewSet(
    ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    DefaultGenericViewSet,
):
    pass


class ReadOnlyModelViewSet(
    ViewSetMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    DefaultGenericViewSet,
):
    pass


class ModelViewSet(
    ViewSetMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    DefaultGenericViewSet,
):
    pass
