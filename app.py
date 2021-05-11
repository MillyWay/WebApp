from flask import Flask
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
    return 'hello'    

@app.route('/naver')
def naver():
    return '네이버'    



if __name__ == '__main__':
    app.run()