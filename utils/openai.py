from django.conf import settings
import openai

openai.api_key = settings.OPENAI_API_KEY


def get_daily_quote():
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": "오늘의 새로운 좋은 글귀 한마디를  100자이내로 생성해주세요. ,",
            }
        ],
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].message["content"].strip()
