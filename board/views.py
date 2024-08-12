from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404, redirect, render

from board.models import BoardPost, Comment, Reply
from main.models import Product



def board(request):
    boards = BoardPost.objects.filter(board_date__lte=datetime.now()).order_by('-board_date')
    board_comments = {}
    for board in boards:
        board_comments[board.board_id] = Comment.objects.filter(board=board).order_by('comment_date')[:2]

    return render(request, "board/board.html", {'boards': boards, 'board_comments': board_comments})


def boardpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        cate = request.POST.get('cate')
        file = request.FILES.get('file')
        board_date = datetime.now()

        if title and content:
            board = BoardPost.objects.create(
                user=user,
                title=title,
                content=content,
                cate=cate,
                file=file,
                board_date=board_date
            )
            return redirect('boardpost_detail', pk=board.pk)
        else:
            error_message = "제목과 내용을 입력해주세요."
            return render(request, "board/board_post.html", {
                'error_message': error_message,
                'title': title,
                'content': content,
                'cate': cate,
            })
    else:
        return render(request, "board/board_post.html")
                
def boardpost_detail(request, board_id):
    user = request.user
    current_user = User.objects.filter(username=user)
    board = get_object_or_404(BoardPost, board_id=board_id)
    comments = Comment.objects.filter(board=board).order_by('comment_date')
    context = {
        'board': board,
        'comments': comments,
        'user': current_user
    }
    return render(request, 'board/board_post_detail.html', context)


def post_delete(request, board_id):
    if request.method == 'GET':
        board = BoardPost.objects.get(board_id=board_id)
        board.delete()
        return redirect('board')

    elif request.method == 'POST':
        return HttpResponse('잘못된 접근 입니다.')



def comments_one(request, board_id):
    if request.method == 'POST':
        board_id = request.board_id
        comment = request.POST.get('comment')
        user = request.user
        comment_date = datetime.now()
        comments = Comment.objects.create(
            board_id=board_id,
            user=user,
            content=comment,
            comment_date= comment_date
            )
        
        print(comments)
        return redirect('boardpost_detail', pk=comments.pk)
    else:
        return render(request, "board/board_post.html")
    


def comments_create(request, pk):
    if request.user.is_authenticated:
        board = get_object_or_404(BoardPost, pk=pk)
        if request.method == 'POST':
            comment_content = request.POST.get('comment')
            user = request.user
            if comment_content:
                comment_date = datetime.now()
                Comment.objects.create(
                    board=board,
                    user=user,
                    content=comment_content,
                    comment_date=comment_date
                )
                return redirect('boardpost_detail', pk=board.pk)
            else:
                # 댓글 작성 실패 시
                comments = Comment.objects.filter(board=board).order_by('comment_date')
                error_message = "댓글 내용을 입력해주세요."
                return render(request, "board/board_post_detail.html", {
                    'board': board,
                    'comments': comments,
                    'error_message': error_message
                })
    else:
        return redirect('main/login.html')


def comments_delete(request, pk, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.user or request.user == comment.board.user:
            comment.delete()
            return redirect('boardpost_detail', pk=pk)
        else:
            return HttpResponse('권한이 없습니다.', status=403)
    else:
        return redirect('main/login.html')


def reply_create(request, board_id, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.method == 'POST':
            reply_content = request.POST.get('reply')
            user = request.user
            if reply_content:
                reply_date = datetime.now()
                Reply.objects.create(
                    comment=comment,
                    user=user,
                    content=reply_content,
                    reply_date=reply_date
                )
                return redirect('boardpost_detail', board_id=board_id)
            else:
                # 답댓글 내용이 비어 있는 경우 처리
                return redirect('boardpost_detail', board_id=board_id)
    else:
        return redirect('main/login.html')


def reply_delete(request, board_id, comment_id, reply_id):
    if request.user.is_authenticated:
        reply = get_object_or_404(Reply, pk=reply_id)
        if request.user == reply.user or request.user == reply.comment.board.user:
            reply.delete()
            return redirect('boardpost_detail', board_id=board_id)
        else:
            return HttpResponse('권한이 없습니다.', status=403)
    else:
        return redirect('main/login.html')
    

def board_search(request):
    q = request.POST.get('q')
    if q:
        board_search = BoardPost.objects.filter(title__icontains = q)
        return render(request, 'board/board_search.html', {'board_search': board_search, 'q':q})
    else:
        return render(request, "board/board.html")
    
def board_show_recipe(request):
    recipes = BoardPost.objects.filter(cate="레시피 공유")
    return render(request,"board/board.html", {'boards': recipes})

def board_show_life(request):
    lives = BoardPost.objects.filter(cate="일상 공유")
    return render(request, "board/board.html", {'boards': lives})
