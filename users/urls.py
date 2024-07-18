from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    # allauth
    path('accounts/', include('allauth.urls')),

    # dj-rest-auth
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('kakao-login/', kakao_login_view, name='kakao-login'),
    # path('kakao-user-info/', kakao_user_info, name='kakao-user-info'),

    path('profile/', ProfileView.as_view(), name='profile'),  # 프로필 URL 추가
]