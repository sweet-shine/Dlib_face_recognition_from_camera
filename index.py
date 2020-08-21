# coding=utf-8
# auther:wangc
# 2020-08-20
from flask import Flask

app = Flask(__name__)


@app.route('/add_face', methods=['GET'])
def add_face():

    return 'hahaa'


@app.route('/generate_features')
def generate_features():
    pass


@app.route('/face_recognition')
def face_recognition():
    pass


if __name__ == '__main__':
    app.run(debug=True)
