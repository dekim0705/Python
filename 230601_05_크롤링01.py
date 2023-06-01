# ❗️ 패키지 설치 : pip3 install beautifulsoup4
#                : pip3 install requests

import requests # HTTP 요청을 보내고 응답을 받는데 사용하는 라이브러리 (get, post, put, delete)
from bs4 import BeautifulSoup # HTML과 XML파일에서 데이터를 추출하는데 사용

# url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
# html = requests.get(url).text
# # print(html) # 모든 정보가 들어옴
# soup = BeautifulSoup(html, "html.parser")
# print(soup)


url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# HTTP Get 요청
response = requests.get(url).text

# HTML 파싱
soup = BeautifulSoup(response, "html.parser")
# print(soup)

# BeautifulSoup에 있는 문법을 이용하여 원하는 정보만 얻기
for loc in soup.select("location") :
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-"*20)
