# 📌 내장 함수 : 파이썬에서 기본적으로 제공하며, import 없이 사용

print(max([1,2,3,4,5,6,7,8,9])) # 9
print(min([1,2,3,4,5,6,7,8,9])) # 1
print(sum([1,2,3,4,5,6,7,8,9])) # 45

ls = [1,2,3,4,5,6,7,8,9]
print(sum(ls) / len(ls))  # 평균 구하는 방법

ls2 = [10,2,33,41,25,6,7,8,9]
print(sorted(ls2))  # 정렬

print(divmod(sum(ls), 5))  # 몫과 나머지 한번에 반환

# 📌 외장 함수 : import해서 사용
import random

# 지정한 범위 내의 임의의 수를 구하는 함수
rand = random.randint(0, 4) # 0 ~ 4 사이의 임의의 값이 생성
print(rand)

rand = random.randrange(0, 4) # 0 ~ 4 사이의 임의의 값이 생성
print(rand)

# 현재 시간 가져오기
    # import datetime
    # print(datetime.datetime.today())
from datetime import datetime
# datetime 내부에서 datetime함수를 가져 옴 -> 장점✨ 접근 경로가 짧아짐 & 라이트하게 가져올 수 있음
print(datetime.today())

datetime.today()            # 현재 날짜 가져오기
datetime.today().year       # 현재 연도 가져오기
datetime.today().month      # 현재 월 가져오기
datetime.today().day        # 현재 일 가져오기
datetime.today().hour       # 현재 시간 가져오기

print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)







