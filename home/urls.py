from django.urls import path
from django.shortcuts import redirect
from .views import HomeViev

urlpatterns = [
    path("", lambda request: redirect("home_page")),
    path("home/", HomeViev.as_view(), name="home_page")
]
