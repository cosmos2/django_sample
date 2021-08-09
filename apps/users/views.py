from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer
from utils.drf.viewsets import ReadOnlyModelViewSet


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()

    serializer_classes = {"list": UserSerializer}

    permission_classes = [IsAuthenticated]
