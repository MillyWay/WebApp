from db import insert_data
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        insert_data(email,pwd)
        return '회원가입 데이터(POST)'
        


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        if email == 'a@a.com' and pwd == '1':
            return "로그인 성공"
      
        else:
            return "아이디 패스워드 확인"
    


@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        search = request.form['fname']
        print("전달된값:", search)
        return '당신이 검색한 키워드(POST)<br>{}입니다'.format(search)


if __name__ == '__main__':
    app.run()