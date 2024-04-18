from django.shortcuts import render, redirect
from django.conf import settings
import openai
from .models import UserBirthday


def get_zodiac_sign(month, day):
    zodiac_dates = [
        (120, "물병자리"),
        (219, "물고기자리"),
        (321, "양자리"),
        (420, "황소자리"),
        (521, "쌍둥이자리"),
        (622, "게자리"),
        (723, "사자자리"),
        (823, "처녀자리"),
        (924, "천칭자리"),
        (1023, "전갈자리"),
        (1123, "사수자리"),
        (1225, "염소자리"),
    ]

    zodiac_sign = next(
        sign for end_date, sign in zodiac_dates if (month * 100 + day) <= end_date
    )
    return zodiac_sign


def fortune(request):
    if not request.user.is_authenticated:
        return redirect("/")

    zodiac_sign = get_zodiac_sign(
        request.user.birth_date.month, request.user.birth_date.day
    )
    horoscope_text = constellation_fortune(request, zodiac_sign)
    # print("운세:", horoscope_text)

    # UserBirthday 모델 인스턴스 생성 및 저장
    horoscope_instance = UserBirthday(
        birth_date=request.user.birth_date,
        zodiac_sign=zodiac_sign,
        horoscope=horoscope_text,
    )
    horoscope_instance.save()

    return render(request, "horoscope.html", {"horoscope": horoscope_text})


def constellation_fortune(request, zodiac_sign):
    if not request.user.is_authenticated:
        return redirect("/")

    openai.api_key = settings.OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": f"{zodiac_sign} 에 맞는 오늘의 운세에 조언이나 충고 해주세요.",
            },
        ],
        temperature=0.7,
        # max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    if response.choices:
        horoscope_text = response.choices[0]["message"]["content"].strip()
        return horoscope_text
    else:
        return "운세를 불러오는 중에 오류가 발생했습니다."
