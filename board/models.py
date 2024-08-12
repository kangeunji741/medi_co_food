from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class BoardPost(models.Model):
    board_id = models.AutoField(primary_key=True, db_comment='게시글 식별자')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, db_comment='회원 식별자')
    cate = models.CharField(max_length=100)
    title = models.CharField(max_length=1500, db_comment='글 제목')
    content = models.TextField(db_comment='글 내용')
    board_date = models.DateTimeField(db_comment='글 작성일자')
    file = models.FileField(null=True, upload_to="uploads/", blank=True, db_comment='글 첨부파일')  # 파일 컬럼 추가

    class Meta:
        db_table = 'board_post'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
        ordering = ['-board_date']  # 최신 글이 위로 오도록 설정

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:boardpost_detail', args=[self.board_id])


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, db_comment='댓글 아이디')
    board = models.ForeignKey(BoardPost, on_delete=models.CASCADE, db_comment='게시글 식별자')  # on_delete 수정
    content = models.TextField(db_comment='댓글 내용')
    comment_date = models.DateTimeField(db_comment='댓글 작성일자')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, db_comment='댓글 작성자')

    class Meta:
        db_table = 'comments'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'

    def __str__(self):
        return self.content

    @property
    def replies(self):
        return self.reply_set.all()


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True, db_comment='답댓글 아이디')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, db_comment='댓글 아이디')  # on_delete 수정
    user = models.ForeignKey(User, on_delete=models.RESTRICT, db_comment='작성자 아이디')
    content = models.TextField(db_comment='답댓글 내용')
    reply_date = models.DateTimeField(db_comment='답댓글 작성일자')

    class Meta:
        db_table = 'reply'
        verbose_name = '답댓글'
        verbose_name_plural = '답댓글'

    def __str__(self):
        return self.content
