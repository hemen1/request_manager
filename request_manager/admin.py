from django.contrib import admin
from .models import Request, Provider

admin.site.register(Provider)
admin.site.register(Request)
