from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = CKEditor5Field("Description", config_name="default")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150)
    image = models.FileField(upload_to="destination/")
    best_time_to_visit = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Package(models.Model):
    title = models.CharField(max_length=230)
    destination= models.ForeignKey(Destination,on_delete=models.CASCADE)
    duration = models.CharField(max_length=30)
    difficulty = models.CharField(max_length=30)
    price = models.IntegerField()
    max_people = models.IntegerField()
    itinerary = CKEditor5Field("Itinerary", config_name="default", blank=True, null=True)
    includes = CKEditor5Field("Includes", config_name="default")
    excludes = CKEditor5Field("Excludes", config_name="default")
    featured_image = models.FileField(upload_to="packages/")

    def __str__(self):
       return self.title

class Booking(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30
    )

    number_of_people = models.PositiveIntegerField()

    travel_date = models.DateField()

    special_requests = models.TextField(
        blank=True,
        null=True
    )

    booked_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,blank=True, null=True, default="pending"
    )

    def __str__(self):
        return f"{self.full_name} - {self.package.title}"

class Tour(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    duration = models.CharField(max_length=50, blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True,blank=True)
    bookings = models.ManyToManyField(Booking, related_name="tours")

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.package.title}"

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.FileField(upload_to="gallery/")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title



class TravelPlan(models.Model):

    HOTEL_CHOICES = [
        ("Budget", "Budget"),
        ("Standard", "Standard"),
        ("Luxury", "Luxury"),
    ]

    TRANSPORT_CHOICES = [
        ("Flight", "Flight"),
        ("Train", "Train"),
        ("Bus", "Bus"),
        ("Cruise", "Cruise"),
    ]

    MEAL_CHOICES = [
        ("Breakfast Only", "Breakfast Only"),
        ("Half Board", "Half Board"),
        ("Full Board", "Full Board"),
        ("All Inclusive", "All Inclusive"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE
    )

    travel_date = models.DateField()

    travelers = models.PositiveIntegerField()

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    hotel = models.CharField(
        max_length=30,
        choices=HOTEL_CHOICES
    )

    transport = models.CharField(
        max_length=30,
        choices=TRANSPORT_CHOICES
    )

    meals = models.CharField(
        max_length=30,
        choices=MEAL_CHOICES
    )

    special_requests = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.destination.name} - {self.travelers} Travelers"




class Payment(models.Model):

    PAYMENT_METHODS = [
        ("esewa", "eSewa"),
        ("cod", "Cash on Delivery"),
    ]

    PAYMENT_STATUS = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    booking = models.OneToOneField(
        "Booking",
        on_delete=models.CASCADE,
        related_name="payment"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="pending"
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.booking} - {self.amount}"