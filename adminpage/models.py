from django.db import models

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
    description = models.TextField()
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
    itinerery = models.CharField(max_length=10000)
    includes = models.CharField(max_length=50000)
    excludes = models.CharField(max_length=50000)
    featured_image = models.FileField(upload_to="packages/")

    def _str_(self):
       return self.title

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    number_of_people = models.PositiveIntegerField()
    travel_date = models.DateField()
    special_requests = models.TextField(blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)

    def __str__(self):
        return f"{self.full_name} - {self.package.title}"

class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    