from django.urls import path
from .views import PackageCreateView, DestinationCreateView, travel_plan,admin_dashboard,admin_login,admin_logout, bookings, booking_edit

urlpatterns = [
    path("login/",admin_login,name="admin_login"),
    path("logout/",admin_logout,name="admin_logout"),
    path('dashboard/',admin_dashboard, name='admin_dashboard'),
    path('packages/create/', PackageCreateView, name='package_create'),
    path('destinations/create/', DestinationCreateView, name='destination_create'),
    path('travel-plans/', travel_plan, name='travel_plan'),
    path('bookings/', bookings, name='bookings'),
    path('bookings/edit/<int:booking_id>', booking_edit, name='booking_edit'),
   
]