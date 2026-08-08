from django.urls import path
from .views import PackageCreateView, DestinationCreateView, travel_plan

urlpatterns = [

    path('packages/create/', PackageCreateView, name='package_create'),
    path('destinations/create/', DestinationCreateView, name='destination_create'),
    path('travel-plans/', travel_plan, name='travel_plan'),
]
