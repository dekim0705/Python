# 📌 while문 
	# 조건이 참인 동안 반복 수행하여 주로 횟수가 정해지지 않은 경우에 사용,
	# 횟수가 정해지지 않은 경우, 반드시 탈출 조건이 필요
	# break & continue
n = int(input("정수 입력 : "))
sum = 0
while n :
    sum += n	# sum = sum + n
    n -= 1		# n-- 같은 증감 연산자가 없어서 명시적으로 1을 빼줘야 함 (복합 대입연산자)
print(sum)		# n이 0이 되면 false가 되기 때문에 while문 빠져나올 수 있음


# 📌 유효값 체크
while True:
    age = int(input("나이를 입력 하세요 : "))
    if 0 < age < 200: break # 정상적으로 값이 입력 되었으므로 반복문을 벗어 난다.
    else: print("나이 입력 범위를 벗어 났습니다.")

    
# 📌 for 요소 in 시퀀스
	# 자바의 향상된 for문과 동일, 시퀀스(리스트, 튜플, 문자열 등)의 각 요소를 순회할 때 사용
fruits = ["apple", "banana", "kiwi"]
for e in fruits : 
    print(e)


# 📌 for 변수 in range(시작값, 종료값, 증감값)
	# 자바의 기본적인 for문과 동일, index사용, 숫자 범위를 순회할 때 사용
n = int(input("정수 입력 : "))
sum = 0
for i in range(1, n+1) :
    sum += i
print(sum)


# 📌 2중 for문 : 구구단 출력 
for i in range(2,10) :	# 9단까지 돌리기! 미만 개념 항상 remember...✨
	for j in range(1, 10) :
		print(f"{i} * {j} = {i*j}")
	print("-"*25)


# 📌 2중 for문과 조건문 활용하기 (별로인 예제...)
n = int(input("정수 입력 : "))
for i in range(0, n) :	# 입력받은 갯수 만큼 순회
	for j in range(0, n) :
		if j % 2 == 0 : print(f"{j}는 짝수")
		else : print(f"{j}는 홀수")
	print()


# ⭐️찍기 : 입력 받은 수 만큼 별 찍기
n = int(input("별 찍기 정수 입력 : "))	# 행을 의미
for i in range(n) :	# 하나만 넣으면 최종값, 0 부터 n 미만까지 💫
	for j in range(i+1) : 
		print("*", end="")	# 별을 옆으로 찍기 위해서 end=""
	print()	# 내부 for문이 끝나면 줄바꿈

n = int(input("reversed 별 찍기 : "))
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()


# 📌 for문에서 continue 사용 
	# continue를 만나면 아래의 문장을 수행하지 않고 반복문의 조건문으로 이동
n = int(input())
for i in range(n) :
	if i % 2 == 0 : continue
	print(i)


# 📌 for문을 역순으로 순회
n = int(input())
for i in range(n, 0 - 1, -1) :	# 미만의 개념이 있으니까 0까지 찍기 위해 0 - 1, 증감값 넣지 않으면 무한대로 돌 수 있음
	print(f"값 : {i}")


# 📌 for문으로 알파벳 출력 하기 : 파이썬은 유니코드 사용
	# ✨ chr : 유니코드값을 입력 받아 코드에 해당하는 문자를 출력
	# ✨ ord : 문자의 유니코드 값을 돌려주는 함수
for i in range(ord("A"), ord("Z")+1) : # 시작값은 65, 종료값은 90+1
    print(chr(i), end=" ")	# 유니코드 값을 입력 받아 문자로 돌려주기


# 📌 학점 구하기 : 성적을 입력 받아 학점 출력 하기 (반복문 사용, 음수가 입력되면 종료, 100 보다 크면 재 입력 요구)
while True :	# 반복문 사용
    score = int(input("점수 입력 : "))
    # 종료 조건
    if score < 0 : break
	# 재입력 요구 조건
    if score > 100:
        print("점수를 잘못 입력 하셨습니다.")
        continue  # 반복문으로 되돌아 가기
    if score >= 90 : grade = "A"
    elif score >= 80 : grade = "B"
    elif score >= 70 : grade = "C"
    elif score >= 60 : grade = "D"
    else : grade = "F"
    print(f"{score}에 대한 학점은 \"{grade}\"입니다.")
    





