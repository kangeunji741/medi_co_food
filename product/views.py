from django.shortcuts import render

from main import models
from django.contrib.auth.models import User  # User 모델 임포트

# Create your views here.
def product(request):
    return render(request, "product/product.html")

