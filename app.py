from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('122.45.215.189', 27017, username="아이디", password="비밀번호")
db = client.dbsparta_plus_week2


@app.route('/')
def main():
    # DB에서 저장된 단어 찾아서 HTML에 나타내기
    return render_template("login.html")


@app.route('/signup')
def signup():
    # API에서 단어 뜻 찾아서 결과 보내기
    return render_template("signup.html")

@app.route('/main')
def search():
    # API에서 단어 뜻 찾아서 결과 보내기
    return render_template("index.html")




@app.route('/detail')
def detail():
    # API에서 단어 뜻 찾아서 결과 보내기
    return render_template("detail.html")


@app.route('/api/save_word', methods=['POST'])
def save_word():
    # 단어 저장하기
    return jsonify({'result': 'success', 'msg': '단어 저장'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    # 단어 삭제하기
    return jsonify({'result': 'success', 'msg': '단어 삭제'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)