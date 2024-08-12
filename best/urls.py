from django.urls import path

from best.views import best_product



urlpatterns = [
    path('', best_product, name='best_product'),
]