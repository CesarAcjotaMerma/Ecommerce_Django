from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Product

# Create your views here.
class ProductListView(generic.ListView):
    template_name='cart/product_list.html'
    queryset = Product.objects.all()

class ProductDetailView(generic.FormView):
    template_name = 'cart/product_detail.html'
    queryset = Product.objects.all()