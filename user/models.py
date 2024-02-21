from django.contrib.auth.models import AbstractUser
from django.db import models

from user.manager import UserManager
from user.validators import password_validator


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(
        max_length=100,
        validators=[password_validator]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
