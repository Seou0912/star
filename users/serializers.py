from rest_framework.views import APIView

from rest_framework import serializers
from django.contrib.auth.models import User
from allauth.socialaccount.helpers import complete_social_login
from rest_framework.exceptions import ValidationError


class SocialLoginSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, data):
        # 소셜 토큰을 이용한 사용자 인증 로직 구현
        request = self.context.get("request")
        token = data.get("token")

        # 여기에 소셜 로그인 검증 로직을 구현합니다.
        # 예: 토큰을 이용해 사용자 정보를 가져오고, 이를 검증하는 과정

        return data

    def create(self, validated_data):
        # 사용자 모델 생성 또는 업데이트 로직 구현
        user, _ = User.objects.get_or_create(**validated_data)
        return user
