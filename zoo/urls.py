from django.urls import path
from zoo import views

urlpatterns = [
    path("", views.home, name="home"),
]