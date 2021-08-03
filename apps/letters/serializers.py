from rest_framework import serializers

from letters.models import Letter
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
        ref_name = "letters_Letter_author"

    def get_email(self, obj):
        return obj.get_email


class LetterSerializer(serializers.ModelSerializer):
    author = _UserSerializer()

    class Meta:
        model = Letter
        fields = (
            "id",
            "title",
            "content",
            "author",
        )
