from django.contrib import admin
from .models import Products

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):  # (AdminManagerMixin, ImportExportMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'stock']