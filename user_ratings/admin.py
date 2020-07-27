from django.contrib import admin
from .models import Item, ItemLineItem

class ItemLineAdminInline(admin.TabularInline):
    model = ItemLineItem


class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemLineAdminInline, )

# Register your models here.
admin.site.register(Item, ItemAdmin)