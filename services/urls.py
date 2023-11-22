from django.urls import path

from .views import ServiceList, CreateContact, CreateContactSuccess


urlpatterns = [
    path("", view=ServiceList.as_view(), name="service-list"),
    path("contact/", view=CreateContact.as_view(), name="contact-create"),
    path(
        "contact/success/",
        view=CreateContactSuccess.as_view(),
        name="contact-create-success",
    ),
]
