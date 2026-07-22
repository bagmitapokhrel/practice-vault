from django.contrib import admin
from .models import Category,Destination, Package

# Register your models here.
admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(Package)


