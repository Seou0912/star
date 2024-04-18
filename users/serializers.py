from rest_framework.views import APIView
from .serializers import UserSerializer


class KakaoLoginView(APIView):
    serializer_class = UserSerializer
