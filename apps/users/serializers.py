from rest_framework import serializers
from taggit.models import Tag

from bookmarks.models import Bookmark
from letters.models import Letter
from users.models import User


class _TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
        )
        ref_name = "users_User_bookmark_set_tags"


class _BookmarkSerializer(serializers.ModelSerializer):
    tags = _TagSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = (
            "id",
            "url",
            "tags",
        )
        ref_name = "users_User_bookmark_set"


class _LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = (
            "id",
            "title",
            "content",
        )
        ref_name = "users_User_letter_set"


class UserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(help_text="아이디 앞 1 자리 제외하고 * 표시")
    bookmark_set = _BookmarkSerializer(
        many=True,
    )
    letter_set = _LetterSerializer(
        many=True,
    )

    class Meta:
        model = User
        fields = (
            "id",
            "nickname",
            "email",
            "bookmark_set",
            "letter_set",
        )

    def get_email(self, obj):
        return obj.get_email
