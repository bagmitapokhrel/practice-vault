from django.urls import path
from .views import PackageCreateView

urlpatterns = [

    path('packages/create/', PackageCreateView, name='package_create'),
]