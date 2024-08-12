"""
URL configuration for teamproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main.views import login

urlpatterns = [
    path("", login, name='login'),
    path("admin/", admin.site.urls),
    path("main/", include('main.urls')),
    path("board/", include('board.urls')),
    path("my/", include('my.urls')),
    path('accounts/', include('allauth.urls')),  # 소셜 어카운트를 이용하였기 때문에 앱 생없이 기능 사용
    path("best/", include('best.urls')),
    path("product/", include('product.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 게시판에 사용자들이 글을 작성하면 여기에 들어감
    # 문제는 디비에는 따로 저장이 안되고 개인 로컬 피시에 저장되기 때문에 시연용 노트북에서만 사진 업로드 할 것, 아니면 어드민에서 처리