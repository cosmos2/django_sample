from django.urls import path, include
from rest_framework.routers import SimpleRouter

from auth.views import AuthViewSet

router = SimpleRouter()
router.register("auth", AuthViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
