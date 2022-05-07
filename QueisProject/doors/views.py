from re import template
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Door, DoorContent, User

class MainView(generic.ListView):
    template_name = "doors/main.html"
    context_object_name = "latest_door_list"

    def get_queryset(self):
        return Door.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]

class DetailView(generic.DetailView):
    model = DoorContent
    template_name = "doors/detail_door.html"

    def get_queryset(self):
        return DoorContent.objects.all()

class ProfileView(generic.DetailView):
    model = User
    template_name = "doors/profile.html"

    def get_queryset(self):
        return User.objects.all()

class MarketView(generic.ListView):
    template_name = "doors/market.html"
    context_object_name = "lastest_doors_list"

    def get_queryset(self):
        return Door.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
    