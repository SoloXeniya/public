from django.contrib import admin
from .models import Product
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["view_image", "title"]

    def view_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src = '{obj.image.url}' width = 200px>")
        else:
            return "No image"

        
