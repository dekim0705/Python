print("안녕하세요")
print(100)
print(33.3333)
print(30+200)

name = "카오스냥"
name1 = '치즈냥'
# ` ` (backtick) 사용 불가

num = 100
print(num)
print(name1)
# Js처럼 타입이 없고 컴파일 하는 순간 형이 결정 됨 
# 스네이크 표기법 사용 (snake_case)

name = "김학생"
email = "user@naver.com"
position = "학생"
addr = "서울시 강남구 역삼동"


print(f""" 
이름 : {name}
메일 : {email}
직업 : {position}
주소 : {addr}
""")
# f는 포맷을 넣을 수 있다는 표시


# 조건문
if True : # 한 줄의 끝을 ; 로 표시하지 않음. : 안쪽으로 들어간다는 뜻
	print("True")
	print("True2")
# print("True2") 들여쓰기 맞추지 않으면 에러
else :
	print("False")

# # 으로 주석 처리
"""
여기는 범위 주석

"""

'''
여기도 범위 주석 
'''

print([1,2,3,4,5,6,7,8,9])
# [] : 파이썬에는 순수 배열은 없고 대신 리스트를 사용 (mutable)
# {} : 딕셔너리에 사용 (Map: key & value)
# () : 튜플(구조분해 구조할당 개념) (immutable)
