from django.shortcuts import render
import json
from .models import Product, ProductCategory
# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        # 'products': json.load(open('products/fixtures/products.json')),
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)


