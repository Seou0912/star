from django.urls import path
from .views import login_view, logout_view, signup, KakaoLoginView, getUserInfo

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
    path("kakao/login/", KakaoLoginView, name="kakao_login"),
    path("kakao/callback/", getUserInfo, name="kakao_login_callback"),
]
