from board.views import board, board_search, board_show_life, board_show_recipe, boardpost, boardpost_detail, comments_create, comments_delete, post_delete, reply_create, reply_delete
from django.urls import path

urlpatterns = [
    path('', board, name='board'),
    path('new/', boardpost, name='boardpost'),
    path('post/<int:board_id>/', boardpost_detail, name='boardpost_detail'),
    path('post/<int:pk>/', boardpost_detail, name='boardpost_detail'),
    path('delete/<int:board_id>/', post_delete, name="post_delete"),
    path('post/<int:pk>/comment/', comments_create, name='comments_create'),
    path('post/<int:pk>/comment/<int:comment_id>/delete/', comments_delete, name='comments_delete'),
    path('post/<int:board_id>/comment/<int:comment_id>/reply/', reply_create, name='reply_create'),
    path('post/<int:board_id>/comment/<int:comment_id>/reply/<int:reply_id>/delete/',reply_delete, name='reply_delete'),
    path('board_search/', board_search, name='board_search'),
    path('life/', board_show_life, name='board_show_life'),
    path('recipe/', board_show_recipe, name='board_show_recipe'),
]
