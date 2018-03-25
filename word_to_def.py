from util import *
import requests


def google_translate_en_to_zh(word, simplified=True):
    try:
        response = requests.post(
            url="https://translation.googleapis.com/language/translate/v2",
            headers={
                "Referer": Google_Referer,
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            },
            data={
                "key": Google_Key,
                "model": "base",
                "q": "{}".format(word),
                "target": "zh-CN" if simplified else "zh-TW",
                "format": "text",
            },
        )
        return response.json()['data']['translations'][0]["translatedText"]
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def oxford_en_to_en(word):
    try:
        response = requests.get(
            url="https://od-api.oxforddictionaries.com/api/v1/entries/en/{}".format(word),
            headers={
                "app_key": oxford_app_key,
                "app_id": oxford_app_id,
                "Accept": "application/json",
            },
        )
        return response.json()['results'][0]["lexicalEntries"]
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

# a = google_translate_en_to_chs("my name is jack")[
#     "translatedText"]  # e.g. {'detectedSourceLanguage': 'en', 'model': 'base', 'translatedText': '我'}

# a = oxford_en_to_en("television")
# if len(a) == 1:
#     print(a[0]["entries"][0]["senses"][0]["definitions"][0])
# else:
#     for j, i in enumerate(a):
#         print("{}.".format(j + 1), i["entries"][0]["senses"][0]["definitions"][0])
