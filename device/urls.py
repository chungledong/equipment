from django.urls import path
from .views import (
    homeView,
    GroupDeviceListView,
    DeviceListView,
    SuppliesOfDeviceListView,
)

app_name = 'device'
urlpatterns = [
    path('', homeView, name='home'),
    path('list-groupdevice/', GroupDeviceListView.as_view(),
         name='list-groupdevice'),
    path('list-device/<pk>', DeviceListView.as_view(),
         name='list-device'),
    path('list-supplies/<pk>', SuppliesOfDeviceListView.as_view(),
         name='list-supplies'),
]
