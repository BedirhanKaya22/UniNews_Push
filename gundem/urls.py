from django.urls import path
from . import views

urlpatterns = [
    path("gundem/", views.gundem, name='gundem'),
]
