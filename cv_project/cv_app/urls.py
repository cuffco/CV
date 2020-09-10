from django.urls import path
from . import views

app_name = 'cv_app'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('services', views.services, name='services'),
    path('projets', views.projets, name='projets'),
]
