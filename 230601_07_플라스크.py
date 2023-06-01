# 파이썬에서 웹 개발을 할 때 Django(장고) 또는 Flask(플라스크)등의 모듈을 사용
    # Flask가 더 가볍기 때문에 웹으로 바로 정보를 띄울 때에는 Flask 사용 추천
# ❗️ 패키지 설치 : pip3 install flask

import requests # HTTP 요청을 보내고 응답을 받는데 사용하는 라이브러리 (get, post, put, delete)
from bs4 import BeautifulSoup # HTML과 XML파일에서 데이터를 추출하는데 사용
from flask import Flask

app = Flask(__name__) # __name__은 현재 모듈 이름을 의미
@app.route("/") # 최상위 코드라는 뜻

def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"
        
    return output


