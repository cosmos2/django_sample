from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as DefaultTokenObtainPairSerializer

from users.models import User


class LoginSerializer(DefaultTokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # custom claims
        token["nickname"] = user.nickname
        token["email"] = user.get_email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "nickname",
            "password",
            "password_2",
            "email",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password_2"]:
            raise serializers.ValidationError({"password": "Check password"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            nickname=validated_data["nickname"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
