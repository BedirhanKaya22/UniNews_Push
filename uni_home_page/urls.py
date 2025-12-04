from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login/", views.login_page, name='login'),
    path("register/", views.register_page, name='register'),
    path("logout/", views.logout_user, name='logout'),
    path("gundem/", views.gundem, name='gundem'),
    path("etkinlikler/", views.etkinlikler, name='etkinlikler'),
    path("duyurular/", views.duyurular, name='duyurular'),
    path("kulup/", views.kulup, name="kulup"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
]
