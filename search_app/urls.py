""""URL patterns for search_app"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
]
