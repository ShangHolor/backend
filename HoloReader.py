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
    def_entocn = word_to_def.google_translate_en_to_zh(word)
    def_entoen_raw = word_to_def.oxford_en_to_en(word)
    if len(def_entoen_raw) == 1:
        def_entoen = def_entoen_raw[0]["entries"][0]["senses"][0]["definitions"][0]
    else:
        def_entoen = ""
        for j, i in enumerate(def_entoen_raw):
            def_entoen += "{}.".format(j + 1), i["entries"][0]["senses"][0]["definitions"][0]
    return def_entoen


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
