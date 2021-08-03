from rest_framework import serializers
from taggit.models import Tag

from bookmarks.models import Bookmark
from users.models import User


class _UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(help_text="아이디 앞 1 자리 제외하고 * 표시")

    class Meta:
        model = User
        fields = (
            "id",
            "nickname",
            "email",
        )
        ref_name = "bookmarks_Bookmark_author"

    def get_email(self, obj):
        return obj.get_email


class _TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
        )


class BookmarkSerializer(serializers.ModelSerializer):
    author = _UserSerializer()
    tags = _TagSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = (
            "id",
            "url",
            "author",
            "tags",
        )
