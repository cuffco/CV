from django.urls import path
from . import views

app_name = 'cv_app'

urlpatterns = [
    path('', views.profil, name='profil'),
    path('services', views.services, name='services'),
    path('projects', views.projects, name='projects'),
    path('contact', views.get_contact, name='contact'),
]
