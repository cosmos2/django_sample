from utils.django.models import DefaultModel
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, is_superuser=False, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nickname, password):
        """
        SuperUser 생성시 사용 (is_staff, is_superuser permissions)
        """
        return self.create_user(email, password=password, nickname=nickname, is_superuser=True)


class User(DefaultModel, PermissionsMixin, AbstractBaseUser):
    nickname = models.CharField("닉네임", max_length=64, blank=False, null=False)
    email = models.EmailField("이메일", max_length=256, unique=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        unique_together = ["email", "nickname"]

    def __str__(self):
        return f"{self.email} / nick: {self.nickname}"

    @property
    def get_email(self):
        front, domain = self.email.split("@")
        anonymized = "".join([char if idx == 0 else "*" for idx, char in enumerate(front)])

        return f"{anonymized}@{domain}"
