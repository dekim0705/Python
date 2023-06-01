# # 📌 모듈 : 함수나 변수 또는 클래스를 모아 놓은 파일
#     # 누군가가 만들어 놓은 파이썬 프로그램, 직접 만들수도 있음
#     # 자주 사용하는 함수등을 별도의 모듈로 만들어 두고 가져다 사용하면 편리

# # ✨ import 모듈 이름 : math.py에 있는 모든 것을 가져오는 것
# import math#

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
# print(math.floor(2.5))
# print(math.ceil(2.5))

# # ✨ from 구문 : 필요한 모듈만 가져오는 것
# from math import sin, cos, tan, floor, ceil

# print(sin(1))
# print(cos(1))
# print(tan(1))
# print(floor(2.5))
# print(ceil(2.5))

# #  as 구문✨
# import math as m

# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))
# print(m.floor(2.5))
# print(m.ceil(2.5))

# 1️⃣ sys : 시스템 관련 정보를 가지고 있는 모듈. 주로 매개변수를 받을 때 사용
import sys

# 명령줄 인수 출력
print("명령줄 인수 : ", sys.argv)

# 스크립트 실행 경로
print("실행 경로 : ", sys.path[0])

# 프로그램 종료
# sys.exit(0) # 운영체제 개입

# 2️⃣ os : 파이썬의 표준 라이브러리, 운영체제와 상호작용하기 위한 기능을 제공
import os

# 현재 작업 디렉토리 가져오기
cwd = os.getcwd()
print("현재 작업 디렉토리 : ", cwd)

# 파일 존재 여부 확인
is_file = os.path.isfile('test.py')
print(is_file)

# 시스템 명령어 출력
os.system("ls -l")