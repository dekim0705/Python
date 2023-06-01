from flask import Flask

app = Flask(__name__) # __name__은 현재 모듈 이름을 의미
@app.route("/")
def hello() :
    return "안녕하세요. 플라스크를 사용해보아요!"