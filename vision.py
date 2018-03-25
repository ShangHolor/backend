import requests
import json
import base64
from util import *


def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content).decode()


def googlevision(base64img):
    try:
        # f = open(path, "rb")
        response = requests.post(
            url="https://vision.googleapis.com/v1/images:annotate",
            params={
                "key": Google_Key,
            },
            headers={
                "Referer": Google_Referer,
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "requests": [
                    {
                        "image": {
                            "content": "{}".format(base64img)
                        },
                        "features": [
                            {
                                "type": "TEXT_DETECTION"
                            }
                        ]
                    }
                ]
            })
        )
        # print('Response HTTP Status Code: {status_code}'.format(
        #     status_code=response.status_code))
        # print('Response HTTP Response Body: {content}'.format(
        #     content=response.content))
        # f.close()

        return response.json()["responses"][0]['textAnnotations']

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
