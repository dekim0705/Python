# 이름 입력
# 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
# 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# 결과는 마지막에 한번에 출력 한다.

name = input("이름 입력 : ")

while True :
    age = input("나이 입력 : ")
    if age.isdigit() : # 입력 받은 문자열이 숫자로 구성되어 있는지 확인
        age = int(age)
        if 0 < age < 200 : break
    print("나이를 잘못 입력 하셨습니다.")   
    # isdigit()과 0<age<200 조건을 둘 다 처리하기 위한 인덴트

while True :
    gender = input("성별 입력 : ")
    if gender == "M" or gender == "m" or gender == "F" or gender == "f" : break
    print("성별을 잘못 입력 하셨습니다.")

while True :
    job = input("직업 입력 : ")
    if job.isdigit() :
        job = int(job)
        if 0 < job < 5 : break
    print("직업을 잘못 입력 하셨습니다.")

if gender == "M" or gender == "m" : gender_prn = "남성"
else : gender_prn = "여성"

job_name = ["", "학생", "회사원", "주부", "무직"]

print("="*5, "회원정보", "="*5)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gender_prn}")
print(f"직업 : {job_name[job]}")

