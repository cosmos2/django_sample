from django.urls import path, include
from rest_framework.routers import SimpleRouter

from bookmarks.views import BookmarkViewSet

router = SimpleRouter()
router.register("bookmarks", BookmarkViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
