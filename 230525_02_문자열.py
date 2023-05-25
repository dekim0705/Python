# 📌 문자열 : 문자로 이루어진 데이터의 집합
	# 1. 큰따옴표(" ")로 감싸기
	# 2. 작은따옴표(' ')로 감싸기
	# 3. 큰따옴표 3개(""" """)로 감싸기
	# 3. 작은따옴표 3개(''' '')로 감싸기
print(""" 안녕하세요
줄바꿈도 가능해요
멋지죵??
""")

# 📌 이스케이프 문자
print("서울시\t강남구\t역삼동")
print("사과\r바나나\r오렌지")

# 📌 인덱싱 : 항상 0에서 부터 시작 
# ✨ 값을 파싱해서 원하는 값을 잘라 낼 때 자주 사용!! 중요! 
jumin = "991120-1234567"
print("성별 : " + jumin[7]) #1
print("태어난 연도 : " + jumin[:2]) 
# 시작 인덱스를 주지 않으면 0에서 시작하고 end는 미만 개념이 있음
print("월 : " + jumin[2:4]) # 2에서 4미만
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])

print("안녕하세요"[0])    #안
print("안녕하세요"[:2])   #안녕
print("안녕하세요"[-3:])  #하세요
print("안녕하세요"[7:])   # 아무것도 나오지 않음

a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3] 
print(b)  #Life

# a[1] = "K" #에러
# ❗️ 리터럴 상수 : 메모리공간에 문자열이 이미 있음 (내부적으로 불변성의 원칙)

# 📌 대소문자 바꾸기
a = "Hello Python Program.."
print(a.upper())  #HELLO PYTHON PROGRAM..
print(b.upper())  #LIFE

# 📌 문자열 변경하기 : replace("","")
input_str = "Hello Python Program"
input_str.replace("Python", "React")
print(input_str) #Hello Python Program
new_str = input_str.replace("Python", "React")
	# 바뀐 문자열을 새로운 변수에 할당해야 함. 불변성의 원칙 기억! 
print(new_str)  #Hello React Program

# 📌 문자열에 표함된 문자 및 문자열 길이 카운트
	# 갯수 세기 : count()
	# 길이 반환 : __len__(), len()
print(input_str.count("l")) # "l" 문자가 몇번 나오는지 카운트
print(len(input_str))       # len() 함수 사용
print(input_str.__len__())  # 문자열에 포함된 내장 함수를 사용

# 📌 문자열 찾기 : find(), rfind(), index()
	# find()  : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 찾지 못하면 -1을 반환
	# index() : 찾은 문자열의 첫 번째 인덱스 반환, 문자열을 찾지 못하면 ValueError라는 예외를 발생 시킴

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))  # 
print(phrase.rfind("가장")) # 뒤에서 부터 해당 문자열을 찾지만 인덱스는 앞에서 부터 계산
print(phrase.index("가장")) 

# 📌 없는 문자열 찾기 
print(phrase.find("나에게"))  # 찾는 결과 없으면 -1
# print(phrase.index("나에게")) # 해당 단어가 없으므로 에러가 발생 

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 📌 문자열 연산자
	# "문자열" + "문자열"
	# "문자열" * 3 : 뒤에 오는 숫자 만큼 문자열을 반복
print("태양고" + str(3))
print("태양고" * 3)


