# 📌 스케쥴링 : 주기적인 작업, 일회성 작업, 클론 작업과 같은 다양한 작업을 자동으로 실행하고 관리하는 데 사용

import schedule
import time
import requests
from bs4 import BeautifulSoup

def perform_web_crawling() :
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job() :
    print("웹 크롤링을 수행 합니다.")
    perform_web_crawling()

# 매일 정해진 시간에 동작 하도록 구현
schedule.every().day.at("10:47").do(job)

while True :
    schedule.run_pending()
    time.sleep(1) # 1초동안 대기했다가 돌기~