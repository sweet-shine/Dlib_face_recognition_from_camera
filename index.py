# coding=utf-8
# auther:wangc
# 2020-08-20
from flask import Flask

import upload_photo

app = Flask(__name__)


@app.route('/upload_photo', methods=['GET', 'POST'])
def add_face():

    return upload_photo.upload_file()


@app.route('/generate_features')
def generate_features():
    pass


@app.route('/face_recognition')
def face_recognition():
    pass


if __name__ == '__main__':
    app.run(debug=True)
