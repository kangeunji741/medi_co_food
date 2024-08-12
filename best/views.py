from django.shortcuts import render

from main.models import Product


# Create your views here.

def best_product(request):
    best_product = Product.objects.all().order_by("-protein")
    return render(request, 'best/best_product.html', {'productList' : best_product})
