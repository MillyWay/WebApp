from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("main.html")  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        # POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된 값:" ,email, pwd)

        

@app.route('/actionpage', methods=['GET', 'POST'])
def actionpage(): 
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        # POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된 값:" ,email, pwd)

    return "회원가입 데이터(POST)"
            

@app.route('/register')
def register():
    return render_template("register.html")         


if __name__ == '__main__':
    app.run()