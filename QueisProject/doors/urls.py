from django.urls import path

from . import views

app_name = "queis"
urlpatterns = [
    path("main", views.MainView.as_view(), name = "main"),
    path("market", views.MarketView.as_view(), name = "market"),
    path("d/<int:pk>", views.DetailView.as_view(), name = "detail_door"),
    path("profile/<int:pk>", views.ProfileView.as_view(), name = "profile"),
]