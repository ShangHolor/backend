from flask import Flask, request
import decode
import word_to_def
import platform

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    img = request.get_json(force=True)
    img_base64 = img['image']
    img_file = decode.load_img_bytes(img_base64)
    word = decode.closest_word(img_file)
    definition = word_to_def.google_translate_en_to_zh(word)
    return definition


if __name__ == '__main__':
    DEBUG = False
    if platform.system() == 'Darwin':
        app.run(
            debug=True
        )
    else:
        app.run(
            host='0.0.0.0',
            port=80,
            debug=DEBUG
        )
