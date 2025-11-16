from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingList.as_view(), name='listing-list'),
    path('<int:pk>/', views.ListingDetail.as_view(), name='listing-detail'),
]