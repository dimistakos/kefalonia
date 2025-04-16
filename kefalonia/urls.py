from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name='main'),
    path('destinations.html', views.destinations, name='destinations'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)