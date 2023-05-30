# 📌 튜플 : 변경할 수 없는(immutable) 시퀀스 자료형. 괄호()를 사용하여 생성 가능
    # ✨ 패킹   : 여러 타입의 데이터를 하나의 튜플이나 리스트로 묶어 선언하는 것
    # ✨ 언패킹 : 하나의 튜플이나 리스트의 요소들을 여러 개의 변수에 나누어 대입하는 것 

# 📌  튜플 정의 하기
person_tuple = ("홍길동", 30, "서울", True) # 튜플
person_tuple2 = "홍길동", 30, "서울", True  # 튜플 ✨괄호()를 생략해도 튜플, 쓰기 불가 특성
person_list = ["홍길동", 30, "서울", True]  # 리스트
person_list[0] = "리스트는 변경 가능"       
# person_tuple[0] = "튜플은 상수, 변경 불가"
# person_tuple2[0] = "튜플은 상수, 변경 불가 22"
print(person_list)


# 📌 튜플 요소에 접근 하기
print(person_tuple[0])
print(person_tuple2[0])


# 📌 튜플 언패킹 하기 (구조 분해와 유사)
name, age, city, tf = person_tuple
print(name)
print(age)
print(city)
print(tf)


# 📌 튜플을 이용한 함수 반환값 다루기
def get_person() :
    name = 'Meredith'
    age = 30
    city = 'London'
    return name, age, city # 필요한 값을 리턴문에 다 걸어주고, 
result = get_person()      # result로 다 받아주면 전부 출력 가능 
print(result) # 📇 ('Meredith', 30, 'London')
print(name)   # 📇 'Meredith'
print(age)    # 📇 30
print(city)   # 📇 'London'
print(name, age, city)  # 📇 홍길동 30 서울


# 📌 기본적인 동작
tp = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 2, 2, 3, 3
print(tp.count(3))  # ✨ 원하는 데이터의 개수를 카운트 하는 함수
print(tp.index(1))  # ✨ 원하는 데이터의 시작 인덱스번호를 알려주는 함수
print(tp.__len__()) # ✨ 튜플 데이터의 개수 (공간의 개수) len(tp)
print(tp.__str__()) # ✨ 문자열 형태로 변환
