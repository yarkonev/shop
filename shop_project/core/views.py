from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    """
    Показывает список товаров.
    """

    model = Product
    template_name = "products.html"
    context_object_name = "products"
