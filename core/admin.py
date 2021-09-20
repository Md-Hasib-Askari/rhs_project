from django.contrib import admin

from .models import IPAddress

@admin.register(IPAddress)
class IPAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'visited_on',]
