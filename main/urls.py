from main import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('life/', views.show_life, name='show_life'),
    path('recipe/', views.show_recipe, name='show_recipe'),
    path('quick/', views.quick, name='quick'),
    path('product_search/', views.product_search, name='product_search'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/like/', views.toggle_like, name='toggle_like'),
    path('query_view/', views.query_view, name='query_view'),
    path('get_element1/', views.get_element1, name='get_element1'),
    path('get_element2/', views.get_element2, name='get_element2'),
    path('get_element3/', views.get_element3, name='get_element3'),
    path('get_photos/', views.get_photos, name='get_photos'),
    path('product_list/<int:p_id>', views.products, name='products')
]
