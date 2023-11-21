from django.views.generic import FormView
from django.urls import reverse_lazy

from users.forms import UserCreationForm


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
