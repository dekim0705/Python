# 📌 입출력
print(712)         # 정수형
print("안녕하세요") # 문자열
print([1,2,3,4,5])  # 리스트형
print(1+2)
print("파"+"이"+"썬") # 결합
print("파""이""썬")
print("파","이","썬") # 콤마(,)는 기본적으로 띄어쓰기가 포함되어 있음
print("파\n\n이\n\n썬") # 줄바꿈 문자 
print("\"안녕하세요\"라고 말했습니다.")

# 📌 end와 sep옵션
print("Hello", end="@") # 한 줄을 마치고 난 뒤에 어떤 문자를 넣을지 설정 가능
print("Hello", end="\t")
print("Hello", end="\n")
print("파이선...")

print(1,2,3,4,5) # separator
print(1,2,3,4,5, sep="\t")

  # 🔍 응용
print("010","1234","5678", sep="-") # 📠 010-1234-5678
year = 2023
month = 5
day = 24
print(year, month, day, sep="/")

# 📌 다양한 출력 스타일
name = "그레이"
age = 30
gender = "여성"
job = "학생"
addr = "미국 시애틀"

# C 언어 스타일 :  %로 서식을 지정하는 형식, 자주 사용되지는 않음
print("="*5, "C 스타일", "="*5) 
print("이름 : %s"%(name))
print("나이 : %d"%(age))
print("성별 : %s"%(gender))
print("직업 : %s"%(job))
print("주소 : %s"%(addr))

# 파이썬 스타일 :  3.6 이전 버전에서 주로 사용
print("="*5, "Python old style", "="*5)
print("이름 : {}".format(name))
print("이름 : {}, 주소 : {}".format(name, addr))
print("나이 : {}".format(age))

# 파이썬 스타일 : 3.6 이후 스타일 (강사님 추천)
print("="*5, "Python new style", "="*5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender}")
print(f"직업 : {job}")
print(f"주소 : {addr}")

# 자바 스타일 (강사님 추천)
print("="*5, "Java style", "="*5)
print("이름 : " + name)
# print("나이 : " + age) 문자열 + 문자열인데 age는 정수라서 에러
print("나이 : " + str(age)) # 문자열로 형변환
print ("성별 : " + gender)

# 📌 출력 포맷 정렬
    # < : 좌측 정렬
    # > : 우측 정렬
    # ^ : 중앙 정렬
print("|{:6}|".format(10))
print("|{:<6}|".format(10))
print("|{:>6}|".format(10))
print("|{:^6}|".format(10))

print(f"|{10:6}|")
num = 10
print(f"|{num:6}|")
print(f"|{num:<6}|")
print(f"|{num:>6}|")
print(f"|{num:^6}|")

# 소수점 이하 자르기
print(f"{3.141592:.2f}")
