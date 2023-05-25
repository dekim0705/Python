# 📌 조건문 : if ~ else
num = int(input("정수를 입력 하세요 : "))
if num % 2 == 0 :
    print("짝수 입니다.")
else : 
    print("홀수 입니다.")
    
# 📌 조건문 : is ~ elif ~ else
n = int(input("정수 입력 : "))
if n > 100 :
    print("100보다 큽니다.")
elif n < 100 :
    print("100보다 작습니다.")
else :
    print("100과 같습니다.")

# 🔍 pass 키워드 : 아무것도 출력하지 않을 때
print("지금 계절은? : ", end='')
season = input()
if season == "spring" : print("봄이 왔어요")
elif season == "summer" : print("여름이 왔어요")
elif season == "fall" or season == "autumn" : print("가을이 왔어요")
elif season == "winter" : print("겨울이 왔어요")
else : pass

age = int(input("나이를 입력 하세요 : "))
if(age > 0 and age < 200) :
    print("정상 입력 입니다.")
else :
    print("잘못 입력 하셨습니다.")
    
if(0 < age < 200) : # 이런식으로도 가능 
    print("정상 입력 입니다.")
else : 
    print("잘못 입력 하셨습니다.")
    
# 📌 중첩 조건식
	#  🔍 회원 가입을 위한 아이디와 패스워드 입력 받기
	# string.find(찾을 문자)
	# string.find(찾을 문자, 시작 Index)
	# string.find(찾을 문자, 시작 Index, 끝 Index)
user = input("아이디 입력 : ")
if len(user) >= 10 : 
    # pass # 구현 중에는 pass로 해놓으면 에러 없이 넘어갈 수 있음
	pw = input("비밀번호 입력 : ")
	if pw.__len__() < 8 or pw.__len__() > 16 :
		print("비밀번호는 8자에서 16자 사이여야 합니다.")
	else : 
		print(f"아이디 	 : {user}")
		print(f"비밀번호 : {pw}")

else : 
    print("아이디는 반드시 10자리 이상이어야 합니다.")