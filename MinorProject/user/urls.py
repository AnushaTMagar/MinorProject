from nturl2path import url2pathname
from django.urls import URLPattern, path

from .import views

urlpatterns = [
    path("home", views.home, name="homePage"),

    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout")
]
