from django.urls import path
from .views import get_product_details

urlpatterns = [
    path("product/", get_product_details),
]
