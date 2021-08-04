from rest_framework.permissions import IsAdminUser

from letters.models import Letter
from letters.serializers import LetterSerializer, LetterCreateSerializer, LetterUpdateSerializer
from utils.drf.viewsets import ModelViewSet


class LetterViewSet(ModelViewSet):
    queryset = Letter.objects.all()
    serializer_classes = {
        "list": LetterSerializer,
        "retreive": LetterSerializer,
        "create": LetterCreateSerializer,
        "LetterUpdateSerializer": LetterUpdateSerializer,
    }
    permission_classes = [IsAdminUser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["author"] = self.request.user
        return context
