from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        default="profile_pictures/default.png",
        blank=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username