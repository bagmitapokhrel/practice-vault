from django.urls import path
from .views import index, package_detail_view,destination, destination_detail, tour, tour_detail, review, about

urlpatterns = [
    path('',index, name='index'),
    path('package/<int:package_id>/', package_detail_view, name='package_detail'),
    path('destination/', destination, name='destination'),
    path('destination_detail/<int:destination_id>/', destination_detail, name='destination_detail'),
    path('tour/', tour, name='tour'),
    path('tour_detail/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('review/', review, name='review'),
    path('about/', about, name='about'),
]