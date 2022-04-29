from re import template
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import QueiContent

class MainView(generic.ListView):
    template_name = "doors/main.html"
    context_object_name = "latest_quei_list"

    def get_queryset(self):
        return QueiContent.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:10]

