from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from users.models import User
from django.conf import settings
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import requests
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/dailyquote/today")

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]

            user = authenticate(email=email, password=password1)

            if user:
                login(request, user)
                return redirect("/dailyquote/today/")
            else:
                form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다.")

        context = {"form": form}
        return render(request, "login.html", context)

    else:
        form = LoginForm()
        context = {"form": form}
        return render(request, "login.html", context)


def logout_view(request):
    logout(request)

    return redirect("/")


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            user = form.save()
            user.birth_date = form.cleaned_data["birth_date"]
            user.mbti = form.cleaned_data["mbti"]
            user.nickname = form.cleaned_data["nickname"]
            user.save()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)
            return redirect("/dailyquote/today/")

    else:
        form = SignupForm()

    context = {"form": form}
    return render(request, "signup.html", context)


from rest_framework import generics


@api_view(["GET"])
@permission_classes(
    [
        AllowAny,
    ]
)
def KakaoLoginView(request):

    # def post(self, request, *args, **kwargs):
    #     code = request.data.get("code")  # 프론트엔드에서 전달받은 인가 코드
    kakao_rest_api_key = settings.KAKAO_REST_API_KEY
    kakao_redirect_uri = settings.KAKAO_REDIRECT_URI
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={0}&redirect_uri={1}"
    url = url.format(kakao_rest_api_key, kakao_redirect_uri)
    res = redirect(url)
    return res


@api_view(["GET"])
@permission_classes(
    [
        AllowAny,
    ]
)
def getUserInfo(reqeust):
    CODE = reqeust.query_params["code"]
    url = "https://kauth.kakao.com/oauth/token"
    res = {
        "grant_type": "authorization_code",
        "client_id": settings.KAKAO_REST_API_KEY,
        "redirect_url": settings.KAKAO_REDIRECT_URI,
        "client_secret": settings.KAKAO_SECRET_KEY,
        "code": CODE,
    }
    headers = {"Content-type": "application/x-www-form-urlencoded;charset=utf-8"}
    response = requests.post(url, data=res, headers=headers)

    token_json = response.json()
    access_token = token_json.get("access_token")

    if not access_token:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    access_token = f"Bearer {access_token}"  # 'Bearer ' 마지막 띄어쓰기 필수

    # kakao 회원정보 요청
    auth_headers = {
        "Authorization": access_token,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    user_info_res = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers=auth_headers
    )
    user_info_json = user_info_res.json()

    kakao_account = user_info_json.get("kakao_account")
    if not kakao_account:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    email = kakao_account.get("account_email")

    # 회원가입 및 로그인
    # res = login_view(email=email)
    # return res

    # if error is not None:
    #     return Response({"message": "Failed to get token"}, status=400)

    # access_token = token_response_json.get(
    #     "Jr9GsscRI76ZOExHb490ij2PWefS6kQzg5QlotFYA83sc7lUE9OFhbj9mzmAKPXRoAAABjvBZdg2m1x-HnlkNwQ"
    # )

    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.post(
        "https://kapi.kakao.com/v2/user/me", headers=headers
    )
    user_info_json = user_info_response.json()
    email = user_info_json.get("kakao_account", {}).get("account_email")
    # if email is None:
    #     return Response(
    #         {"message": "Email not provided"}, status=status.HTTP_400_BAD_REQUEST
    #     )

    # 사용자 정보를 기반으로 내부 처리 (예: 사용자 생성 또는 업데이트)
    # user, created = User.objects.get_or_create(email=email)
    # if created:
    #     user.nickname = user_info_json.get("properties", {}).get("profile_nickname")
    #     user.birth_date = user_info_json.get("kakao_account", {}).get("birthday")
    #     user.save()
    return redirect("/dailyquote/today/")

    return Response(
        {"message": "User logged in successfully"}, status=status.HTTP_200_OK
    )
    try:
        # nickname = "dog"
        return redirect("/dailyquote/today/")
    except User.DoesNotExist:
        # 사용자가 존재하지 않는 경우의 처리
        pass


# naver 로그인


@api_view(["GET"])
@permission_classes([AllowAny])
def NaverLoginView(request):
    naver_client_id = settings.NAVER_CLIENT_ID
    redirect_uri = (
        "http://127.0.0.1:8000/naver/callback/"  # 네이버에 등록한 리다이렉트 URI 사용
    )
    state_token = "state_token"  # 상태 토큰은 랜덤한 값으로 생성
    url = f"https://nid.naver.com/oauth2.0/authorize?client_id={naver_client_id}&response_type=code&redirect_uri={redirect_uri}&state={state_token}"
    res = redirect(url)
    return res


@api_view(["GET"])
@permission_classes([AllowAny])
def getUserInfo2(request):
    CODE = request.query_params["code"]
    url = "https://nid.naver.com/oauth2.0/token"
    client_id = settings.NAVER_CLIENT_ID
    client_secret = settings.NAVER_CLIENT_SECRET
    redirect_uri = (
        "http://127.0.0.1:8000/naver/callback"  # 네이버에 등록한 리다이렉트 URI 사용
    )
    res = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": CODE,
        "redirect_uri": redirect_uri,
    }
    response = requests.post(url, data=res)

    token_json = response.json()
    access_token = token_json.get("access_token")

    if not access_token:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # 네이버 API로 사용자 정보를 가져오는 요청
    user_info_res = requests.get(
        "https://openapi.naver.com/v1/nid/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info_json = user_info_res.json()
    naver_account = user_info_json.get("response", {})

    email = naver_account.get("email")
    if not email:
        return Response(
            {"message": "Email not provided"}, status=status.HTTP_400_BAD_REQUEST
        )

    # 사용자 정보를 저장하거나 필요한 처리를 진행한 후 리다이렉트
    return redirect("/dailyquote/today/")
