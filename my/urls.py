from my import views
from my.views import my
from django.urls import path


urlpatterns = [
    path('', my, name='my'),
    path('my/<int:user_id>', my, name='my'),
    path('ajax/logout/', views.ajax_logout, name='ajax_logout'),
    path('my_post/<int:user_id>', views.my_post, name='my_post'),
    path('my_posts/', views.my_posts, name='my_posts'),  # 수정된 부분
    path('my_liked_products/', views.my_liked_products, name='my_liked_products'),
]