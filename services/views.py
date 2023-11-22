from typing import Any, Dict
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy

from .models import Service
from .forms import ContactForm


class ServiceList(ListView):
    model = Service

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context


class CreateContact(FormView):
    form_class = ContactForm
    template_name = "services/contact_form.html"
    fields = (
        "name",
        "email",
        "area",
        "content",
    )
    success_url = reverse_lazy("contact-create-success")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CreateContactSuccess(TemplateView):
    template_name = "services/contact_form_success.html"
