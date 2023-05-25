# 📌 자료형이란? 데이터를 저장하기 위해 미리 만들어진 데이터의 형태
    # 문자열, 숫자(정수 & 실수), Boolean

# 📌 변수
	# 파이썬에서 데이터형은 값이 대입될 때 결정 됨

# 📌 한 번에 변수에 값 할당하기
a = b = c = 1
print(a,b,c)

a,b,c, = 1, True, "이름"
print(a, b, c)

# 📌 변수의 타입 확인 : type() 함수 이용
age = 100
score = 95.67
is_adult = True
gender = "Male"
print(type(age))
print(type(score))
print(type(is_adult))
print(type(gender))

# 📌 형변환
	# 선언된 변수에 값이 할당되는 순간에 형이 결정되고 이 후 다른 데이터형으로 변경하는 것을 의미 함
# print(10 + "10") # 에러 
print(10 + int("10")) #20
print("나이 : " + str(33))
print(f"나이 : {33}")

a, b = 10, "20"
print(a + int(b))

x, y, z = 0, 10, None, ""
print(bool(x)) # 자바를 제외한 모든 언어는 0을 제외한 정수값은 True
print(bool(y))
print(bool(z))
