from django.urls import path
from adminpage import views as adminpage_views
import adminpage
from .import views
from .views import search
from .views import index, guides, travel_quiz, guide_booking,guide_detail,guide_booking, guide_booking_success, gallery, travel_map, package_detail_view, wishlist, trip_builder_success, add_to_wishlist,remove_from_wishlist, destination,gear_checklist, destination_detail, tour, tour_detail, review, about, contact, package, booking

urlpatterns = [
    path('',index, name='index'),
    path('package/', package, name='package'),
    path('package/<int:package_id>/', package_detail_view, name='package_detail'),
    path('destination/', destination, name='destination'),
    path('destination_detail/<int:destination_id>/', destination_detail, name='destination_detail'),
    path('tour/', tour, name='tour'),
    path('tour_detail/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('review/', review, name='review'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('search/', search, name='search'),
    path('booking/<int:package_id>', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('review/', review, name='review'),
    path('gear_checklist/', gear_checklist, name='gear_checklist'),
    path('travel_map/', travel_map, name='travel_map'),
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist/add/<int:package_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:package_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('trip_builder_success/', trip_builder_success, name='trip_builder_success'),
    path('trip_builder/',adminpage_views.trip_builder, name='trip_builder'),
    path('guides/',guides, name='guides'),
    path('guide_booking/<int:guide_id>/', guide_booking, name='guide_booking'),
    path('guide/<int:guide_id>/',guide_detail, name='guide_detail'),
    path('guide/booking/success<int:guide_id>/', guide_booking_success, name='guide_booking_success'),
    path('travel_quiz/', travel_quiz, name='travel_quiz'),
    path("travel-assistant/", views.travel_assistant, name="travel_assistant"),
    
]