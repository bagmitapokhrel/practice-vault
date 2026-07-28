from django.urls import path
from .views import PackageCreateView, DestinationCreateView

urlpatterns = [

    path('packages/create/', PackageCreateView, name='package_create'),
    path('destinations/create/', DestinationCreateView, name='destination_create'),
]