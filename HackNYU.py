import os
from flask import Flask, jsonify, request
import decode, word_to_def
from flask import Flask, request, url_for, send_from_directory

# from werkzeug import secure_filename

app = Flask(__name__)

# @app.route('/upload', methods=['POST'])
# def upload():
#     base64img = request.form["base64img"]
#     closestword = decode.closest_word(base64img)
#     response = {
#         "bol": "true",
#         "word": "closest_word",
#         "def": "....",
#     }
#     f = open("")
#     return jsonify(response)


# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# # app.config['UPLOAD_FOLDER'] = os.getcwd()
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=upload>
    </form>
    '''



# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.form)
        # file = request.get_json(force=True)
        # for k in file.keys():
        #     print(len(file[k]))

        # print(len(file['image']))
        return "ok"
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(filename)
        #     file_url = url_for('uploaded_file', filename=filename)
        #     return html + '<br><img src=' + file_url + '>'
    return html


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80,
        debug=True
    )
