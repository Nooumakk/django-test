from django.contrib import admin
from .models import Feadback


class AdminFeadback(admin.ModelAdmin):
    list_display = ("name", "email")

admin.site.register(Feadback, AdminFeadback)
