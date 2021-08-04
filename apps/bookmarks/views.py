from rest_framework.permissions import IsAuthenticated

from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer, BookmarkCreateSerializer, BookmarkUpdateSerializer
from utils.drf.viewsets import ModelViewSet


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

    serializer_classes = {
        "list": BookmarkSerializer,
        "retrieve": BookmarkSerializer,
        "create": BookmarkCreateSerializer,
        "update": BookmarkUpdateSerializer,
    }
    permission_classes = [IsAuthenticated]
