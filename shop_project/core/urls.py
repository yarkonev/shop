from django.urls import path
from .views import ProductListView

app_name = "core"

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
]
