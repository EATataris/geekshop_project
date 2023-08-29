from django.shortcuts import render
import json

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open('products/fixtures/products.json') as f:
        data = json.load(f)

    context = {
        'title': 'GeekShop - Каталог',
        'products': data,
    }
    return render(request, 'products/products.html', context)


