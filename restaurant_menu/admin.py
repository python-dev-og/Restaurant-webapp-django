from django.contrib import admin
from .models import Item


class MenuItemAmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAmin)
