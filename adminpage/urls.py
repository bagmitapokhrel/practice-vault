from django.urls import path
from .views import PackageCreateView

urlspatterns = [

    path('packages/create/', PackageCreateView(), name='package_create'),
]