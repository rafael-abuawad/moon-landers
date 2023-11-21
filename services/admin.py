from django.contrib import admin

from .models import Tag, Service, Contact

admin.site.register([Tag, Service, Contact])
