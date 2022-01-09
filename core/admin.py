from django.contrib import admin

# Register your models here.
from core.models import Request



@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']
    list_per_page = 10