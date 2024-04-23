from django.shortcuts import render
from django.utils import timezone
from .models import DailyQuote
from utils.openai import get_daily_quote


def daily_quote(request):
    today = timezone.now().date()  # 오늘 날짜

    # 오늘 날짜에 대한 명언이 이미 있는지 확인
    quote_obj, created = DailyQuote.objects.get_or_create(date=today)

    if created:
        quote_obj.quote = get_daily_quote()  # 새 명언으로 업데이트
        quote_obj.save()

    return render(request, "daily.html", {"quote": quote_obj.quote})
