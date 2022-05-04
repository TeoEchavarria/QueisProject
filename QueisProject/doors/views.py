from re import template
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import Quei, QueiContent, User

class MainView(generic.ListView):
    template_name = "doors/main.html"
    context_object_name = "latest_quei_list"

    def get_queryset(self):
        return Quei.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]

class DetailView(generic.DetailView):
    model = QueiContent
    template_name = "doors/detail_door.html"

    def get_queryset(self):
        return Quei.objects.filter(pub_date__lte=timezone.now())

class ProfileView(generic.DetailView):
    model = User
    template_name = "doors/profile.html"

    def get_queryset(self):
        return User.objects.all()