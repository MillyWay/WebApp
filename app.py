from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <body>

    <h1>웹 앱 프로그래밍</h1>

    <p><a href="http://127.0.0.1:5000/hello">헬로 페이지</a></p>

    <p><a href="http://127.0.0.1:5000/naver">네이버 페이지</a></p>

    </body>
    </html>

    '''

@app.route('/hello')
def hello():
    return render_template("main.html")  

@app.route('/naver')
def naver():
    return render_template("naver.html")   

@app.route('/search', methods=['GET', 'POST'])
def search(): 
    if request.method == 'GET':
        return "데이터를 받아주는 페이지"
    else:
        # POST로 들어오는 데이터를 받아보자
        search = request.form['fname']
        print("전달된 값:" ,search)
        return "당신이 검색한 키워드 (POST)<br>{}입니다.".format (search)


if __name__ == '__main__':
    app.run()