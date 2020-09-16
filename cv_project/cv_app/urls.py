from django.urls import path
from . import views

app_name = 'cv_app'

urlpatterns = [
    path('profil', views.profil, name='profil'),
    path('', views.services, name='services'),
    path('projects', views.projects, name='projects'),
    path('contact', views.get_contact, name='contact'),
]
