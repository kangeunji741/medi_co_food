from django.contrib import admin

from board.models import BoardPost, Comment, Reply

# Register your models here.
class BoardPostAdmin(admin.ModelAdmin):
    list_display = ['board_id', 'user','title','board_date' ]
admin.site.register(BoardPost, BoardPostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["board","comment_date","content","user"]
admin.site.register(Comment, CommentAdmin)



class ReplyAdmin(admin.ModelAdmin):
    list_display = ["comment","reply_date","content","user"]
admin.site.register(Reply, ReplyAdmin)
