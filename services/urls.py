from django.urls import path

from .views import ServiceList


urlpatterns = [
    path("", view=ServiceList.as_view(), name="service-list"),
]
