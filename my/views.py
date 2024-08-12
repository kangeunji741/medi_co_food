from django.shortcuts import render
from django.contrib.auth.models import User  # User 모델 임포트
from django.http import JsonResponse

from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
# views.py
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from yaml import serialize

from board.models import BoardPost

from main.models import Product, Like

@login_required
def my(request):
    user = request.user
    username = user.username
    email = user.email

    context = {
        'username': username,
        'email': email,
    }
    return render(request, 'my/my.html', context)

@login_required
def my_post(request,user_id):
    user = request.user
    my_post = BoardPost.objects.filter(user_id=user_id)
    return render(request,"my/my_post.html",{"my_post":my_post})

@csrf_exempt
def ajax_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)

@login_required
def my_posts(request):
    user = request.user
    boards = BoardPost.objects.filter(user=user).order_by('-board_date')
    posts_data = [{
        'title': board.title,
        'content': board.content,
        'cate': board.cate,
        'board_date': board.board_date.strftime('%Y-%m-%d'),
        'file_url': board.file.url if board.file else None
    } for board in boards]
    return JsonResponse({'posts': posts_data})


@login_required
def board(request):
    user_id = request.GET.get('user_id')  # URL 쿼리 매개변수로부터 사용자 아이디 가져오기
    if user_id:
        posts = BoardPost.objects.filter(user_id=user_id)  # 해당 사용자가 작성한 게시글만 가져오기
    else:
        posts = BoardPost.objects.all()  # 모든 게시글 가져오기

    context = {
        'posts': posts
    }
    return render(request, 'board/board.html', context)

def my_liked_products(request):
    if request.user.is_authenticated:
        # 현재 로그인한 사용자가 좋아요를 누른 상품들의 ID를 가져옵니다.
        liked_products = Like.objects.filter(user=request.user).values_list('product_id', flat=True)
        # 해당 상품들의 정보를 가져옵니다.
        products = Product.objects.filter(product_id__in=liked_products)
        # 필요한 필드들을 선택하여 직렬화합니다.
        serialized_products = list(products.values('product_id', 'product_name', 'image_url'))
        return JsonResponse({'products': serialized_products})
    else:
        return JsonResponse({'error': 'User is not authenticated'}, status=403)
# 사용자의 id를 지정하여 User 모델에서 사용자 정보를 가져옵니다.
user_id = 1  # 가져올 사용자의 id를 지정합니다.
user = User.objects.get(id=user_id)

# 사용자의 username과 email을 출력합니다.
print(user.username)
print(user.email)

