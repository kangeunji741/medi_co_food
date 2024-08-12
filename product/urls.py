
from product.views import product
from django.urls import path


urlpatterns = [
    path('', product, name='product'),]