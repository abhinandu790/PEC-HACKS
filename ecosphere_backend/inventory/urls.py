from django.urls import path
from .views import scan_and_store, get_inventory

urlpatterns = [
    path("scan/", scan_and_store),
    path("list/", get_inventory),
]
