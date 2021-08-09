from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenViewBase

from auth.serializers import LoginSerializer, RegisterSerializer
from users.models import User
from utils.drf.viewsets import CreateModelViewSet


class AuthViewSet(TokenViewBase, CreateModelViewSet):
    queryset = User.objects.all()
    serializer_classes = {
        "login": LoginSerializer,
        "register": RegisterSerializer,
    }
    permission_classes = [AllowAny]

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        pass

    @action(methods=["POST"], detail=False)
    def login(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @action(methods=["POST"], detail=False)
    def register(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
