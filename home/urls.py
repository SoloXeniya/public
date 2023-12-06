from django.urls import path
from .views import index, add_product

urlpatterns = [
    path("", index),
    path("add_product/", add_product),
]


