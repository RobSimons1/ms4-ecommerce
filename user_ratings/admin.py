from django.contrib import admin
from .models import Item, ReviewLineItem

class ReviewLineAdminInline(admin.TabularInline):
    model = ReviewLineItem


class ReviewAdmin(admin.ModelAdmin):
    inlines = (ReviewLineAdminInline, )

# Register your models here.
admin.site.register(Item, ReviewAdmin)