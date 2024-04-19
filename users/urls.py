from django.urls import path
from .views import *

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
    path("kakao/login/", KakaoLoginView, name="kakao_login"),
    path("kakao/callback/", getUserInfo, name="kakao_login_callback"),
    path("naver/login/", NaverLoginView, name="naver_login"),
    path("naver/callback/", getUserInfo2, name="naver_login_callback"),
]
