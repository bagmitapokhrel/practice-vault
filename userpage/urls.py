from django.urls import path
from .views import index, package_detail_view,destination, destination_detail

urlpatterns = [
    path('',index, name='index'),
    path('package/<int:package_id>/', package_detail_view, name='package_detail'),
    path('destination/', destination, name='destination'),
    path('destination_detail/<int:destination_id>/', destination_detail, name='destination_detail')
]