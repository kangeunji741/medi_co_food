from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from board.models import BoardPost
from main.models import DiseaseCategory, Like, Product
import openai
from main.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    posts = BoardPost.objects.all()
    return render(request, "main/main.html", {'posts':posts})

def product_detail(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    is_liked = False

    if request.user.is_authenticated:
        is_liked = Like.objects.filter(user=request.user, product=product).exists()
    diabetes_products = Product.objects.filter(patient_category='당뇨')
    total_sugars = sum([p.sugars for p in diabetes_products])
    diabetes_count = diabetes_products.count()
    avg_sugars = total_sugars / diabetes_count if diabetes_count > 0 else 0

    kidney_products = Product.objects.filter(patient_category='신장질환')
    total_calorie = sum([p.calorie for p in kidney_products])
    kidney_count = kidney_products.count()
    avg_calorie = total_calorie / kidney_count if kidney_count > 0 else 0

    cancer_products = Product.objects.filter(patient_category='암질환')
    total_protein = sum([p.protein for p in cancer_products])
    cancer_count = cancer_products.count()
    avg_protein = total_protein / cancer_count if cancer_count > 0 else 0

    return render(request, "main/product_detail.html", {
        'product': product,
        'avg_sugars': avg_sugars,
        'avg_calorie': avg_calorie,
        'avg_protein': avg_protein,
        'is_liked':is_liked
    })


def login(request):
    return render(request, "main/login.html")

def show_recipe(request):
    recipes = BoardPost.objects.filter(cate="레시피 공유")
    return render(request, "main/main.html", {'posts': recipes})

def show_life(request):
    lives = BoardPost.objects.filter(cate="일상 공유")
    return render(request, "main/main.html", {'posts': lives})

# OpenAI API 키 설정
openai.api_key = 'sk-proj-5SlbdQXgf5ld8EGnvLaaT3BlbkFJW2ScUem0JwU3bmasBoX5'

def get_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

@csrf_exempt
def query_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if not prompt:
            return JsonResponse({'response': 'No prompt provided'}, status=400)
        try:
            response = get_completion(prompt)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'response': f'Error: {str(e)}'}, status=500)
    return render(request, 'main/query_view.html')

def quick(request):
    disease_names = DiseaseCategory.objects.values_list("disease_name", flat=True).distinct()
    products = Product.objects.all()  # 모든 제품 정보를 가져옴
    return render(request, 'main/quick.html', {"disease_names": disease_names, "products": products})

@csrf_exempt
def get_element1(request):
    if request.method == 'POST':
        element1_list = Product.objects.values_list("element1", flat=True).distinct()
        return JsonResponse(list(element1_list), safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_element2(request):
    if request.method == 'POST':
        element1 = request.POST.get('element1')
        element2_list = Product.objects.filter(element1=element1).values_list("element2", flat=True).distinct()
        return JsonResponse(list(element2_list), safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_element3(request):
    if request.method == 'POST':
        element2 = request.POST.get('element2')
        element3_list = Product.objects.filter(element2=element2).values_list("element3", flat=True).distinct()
        return JsonResponse(list(element3_list), safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_photos(request):
    if request.method == 'POST':
        disease_name = request.POST.get('disease_name')
        element1 = request.POST.get('element1')
        element2 = request.POST.get('element2')
        image_data = Product.objects.filter(dcate__disease_name=disease_name, element1=element1, element2=element2).values_list('image_url', 'product_name','product_id')
        # 이미지 URL과 제품 이름을 함께 반환
        image_urls = [{'photoUrl': url, 'productName': name, 'productId':pid} for url, name, pid in image_data]
        return JsonResponse(image_urls, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def products(request,  p_id):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'productList': products,'p_id':p_id})

def product_search(request):
    q = request.POST.get('q')
    if q:
        product_search1 = Product.objects.filter(product_name__icontains=q)
        product_search2 = Product.objects.filter(patient_category__icontains=q)
        context = {
            "product_search1": product_search1,
            "product_search2": product_search2,
            "q": q,
        }
        return render(request, 'main/product_search.html', context)
    else:
        return render(request, "main/product_search.html")



def toggle_like(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Like.toggle_like(request.user, product)
    return redirect('product_detail', product_id=product_id)

# @login_required
# def like_toggle(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     user = request.user
#     is_liked = Like.toggle_like(user, product)
#     return JsonResponse({'is_liked': is_liked})

# @login_required
# def like_toggle(request, product_id):0
#     product = get_object_or_404(Product, pk=product_id)
#     user = request.user
#     like, created = Like.objects.get_or_create(user=user, product=product)

#     if not created:
#         like.delete()
#         is_liked = False
#     else:
#         is_liked = True

#     return JsonResponse({'is_liked': is_liked})