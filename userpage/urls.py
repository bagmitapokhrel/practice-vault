from django.urls import path
from .views import search
from .views import index, gallery, package_detail_view,destination,gear_checklist, destination_detail, tour, tour_detail, review, about, contact, package, booking

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
]