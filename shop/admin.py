from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin


# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ("name",)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ["name", "price", "available", ]
    list_filter = ("category", "available", "price")
    list_editable = ("price", "available")

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
