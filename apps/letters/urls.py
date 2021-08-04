from django.urls import path, include
from rest_framework.routers import SimpleRouter

from letters.views import LetterViewSet

router = SimpleRouter()
router.register("letters", LetterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
