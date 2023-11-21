from django.views.generic import ListView

from .models import Service


class ServiceList(ListView):
    model = Service
