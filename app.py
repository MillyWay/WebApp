import db
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

app.secret_key = b'aaa!111/'

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
        db.insert_data(email,pwd)
        return '회원가입 데이터(POST)'
        


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값:", email, pwd)
        ret = db.get_data(email,pwd)
        if ret != 'None':
            session['email'] = email
            return "로그인 성공"
        else:
            return "로그인 실패"
    


@app.route('/naver')
def naver():
    if 'email' in session:
        return render_template("naver.html")
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

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