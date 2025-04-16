from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('destinations.html', views.destinations, name='destinations'),
]