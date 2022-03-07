from django.urls import path
from .views import (
    homeView,
    GroupSuppliesListView,
    SuppliesListView,
    SearchForm,
)

app_name = 'supplies'
urlpatterns = [
    path('', homeView, name='home'),
    path('list-groupsupplies/', GroupSuppliesListView.as_view(),
         name='list-groupsupplies'),
    path('list-supplies/<pk>/', SuppliesListView.as_view(),
         name='list-supplies'),
]
