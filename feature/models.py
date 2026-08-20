from django.db import models
from django.contrib.auth.models import User
from adminpage.models import Destination
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class TrekPermit(models.Model):

    trek_name = models.CharField(
        max_length=150
    )

    nationality = models.CharField(
        max_length=50
    )

    permit_name = models.CharField(
        max_length=150
    )

    fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fee_type = models.CharField(
        max_length=50,
        choices=[
            ("fixed", "Fixed"),
            ("daily", "Per Day"),
        ]
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.permit_name

class TrekRoutePoint(models.Model):

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE
    )

    day = models.PositiveIntegerField()

    location = models.CharField(
        max_length=150
    )

    altitude = models.PositiveIntegerField()

    distance = models.FloatField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.location} - Day {self.day}"

class Guide(models.Model):

    name = models.CharField(
        max_length=150
    )

    photo = models.ImageField(
        upload_to="guides/"
    )

    bio = models.TextField()

    languages = models.CharField(
        max_length=300
    )

    experience_years = models.PositiveIntegerField()

    specialization = models.CharField(
        max_length=200
    )

    verified = models.BooleanField(
        default=False
    )

    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name
