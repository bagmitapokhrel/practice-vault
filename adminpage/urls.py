from django.urls import path
from .views import PackageCreateView, DestinationCreateView, TourCreateView, travel_plan,admin_dashboard,admin_login,admin_logout, bookings, booking_edit, destination_list, destination_edit, package_list, package_edit, tour_list

urlpatterns = [
    path("login/",admin_login,name="admin_login"),
    path("logout/",admin_logout,name="admin_logout"),
    path('dashboard/',admin_dashboard, name='admin_dashboard'),
    path('packages/create/', PackageCreateView, name='package_create'),
    path('destinations/create/', DestinationCreateView, name='destination_create'),
    path('tours/create/', TourCreateView, name='tour_create'),
    path('travel-plans/', travel_plan, name='travel_plan'),
    path('bookings/', bookings, name='bookings'),
    path('bookings/edit/<int:booking_id>', booking_edit, name='booking_edit'),
    path('destination_list/', destination_list, name='destination_list'),
    path('destination_list/edit/<int:destination_id>/', destination_edit, name='destination_edit'),
    path('package_list/', package_list, name='package_list'),
    path('package_list/edit/<int:package_id>/', package_edit, name='package_edit'),
    path('tour_list/', tour_list, name='tour_list'),
    path('tour_list/edit/<int:tour_id>/', tour_list, name='tour_edit'),
   
]