from django.urls import path

from . import views

app_name = "queis"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("main", views.MainView.as_view(), name = "main"),
]