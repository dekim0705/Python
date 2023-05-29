# 📌 리스트 
    # 원소(Element)들이 연속적으로 저장되는 형태의 자료형
    # 동적으로 크기가 변경 됨
    # 저장되는 요소들이 모두 같은 자료형일 필요는 없음
    # Mutable 객체 (읽고 쓰기가 가능), []

# ❗️ 리스트의 기본 형태
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'apple', True, 3.14, [1,2,3,4,5]]
empty = []

# ❗️ 변수 사용 대비 이점
kor, eng, mat = map(int, input("성적 입력 : ").split())
tot = kor + eng + mat
print(f"평균: {tot / 3}")

score = list(map(int, input("성적 입력 : ").split()))
print(f"평균 : {sum(score)/len(score)}")

# ❗️ 리스트 만들기
odd = [1, 3, 5, 7, 9]
a = []  # 비어 있는 리스트 생성 가능
b = [1, 2, 3]
c = ['seoul', 'gangnamg', 'suwon', 'incheon', [1, 2, 3, 4, 5], ["김학생", "이학생", "박학생"]]
d = [1004, 'jeju', 2048, 'busan']
e = ["test", True, False]

print(e[2])
print(c[1:3])   # 리스트 슬라이싱
print(c[3])
# print(a[0]) # IndexError : list index out of range
print(len(odd))         # 길이 확인
print(odd.__len__())    # 길이 확인
print(c[0][1])  # 2차원 배열로 0번째의 1번째 출력
print(c[4][4])
print(c[5][0][0])


# ❗️ 리스트 연산자 : 연결(+), 반복(*)
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("list_a = ", list_a)
print("list_b = ", list_b)

print(list_a * 3)
print(list_a + list_b)


# ❗️ 리스트 요소 추가하기 (성능이 많이 차이 남! Big-O 표기법 참고)
    # ✨ append(val)        : 리스트의 끝에 값을 추가하는 함수
    # ✨ insert(index, val) : 특정 위치에 값을 추가하는 함수
list_a = [1, 2, 3]
list_a.append(4)
list_a.append(10)
list_a.insert(1, 22)
print(list_a)


# ❗️ 리스트 요소 제거하기
    # ✨ list.pop(index)   : 인덱스를 쓰지 않으면 마지막 인덱스를 반환 후 삭제   
    #                      : 인덱스가 있으면 인덱스 위치의 데이터 삭제
    # ✨ list.remove(val)  : 동일한 값이 여러개 있는 경우 낮은 인덱스의 값 제거
    # ✨ list.clear()      : 모든 값을 삭제하고 빈 리스트만 남김
    # ✨ del list[index]   : 해당 값 제거

list_all = [0,1,2,3,4,5,6,8,9,"a", "b", "c", "d", "e", "f", "korea", "seoul", "gangnam"]

print(list_all)
list_all.pop()  # 인덱스가 없으므로 마지막 요소 제거
print(list_all)
list_all.pop(8) # 인덱스로 제거
# print(list_all.pop(8))
print(list_all)
list_all.insert(8, 9)
print(list_all)
del list_all[15]
print(list_all)

list_all.clear()
print(list_all)


# 📌 중복 제거 : 리스트내에 중복된 값을 제거
my_list = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
new_list = []
for e in my_list :          # iterate(?) the elements of 'my_list'
    if e not in new_list :  # if the element is not in 'new_list', 
        new_list.append(e)  # add the element
print(new_list)


# 📌 정렬
arr = [1, 4, 5, 666, 999, 1000, 2, 3, 4, 5]
arr.sort()  # 오름차순 정렬
print(arr)
arr.sort(reverse=True)  # 내림차순 정렬
print(arr)


# 📌 리스트의 모든 원소 스캔하기 : for반복문에 len()함수를 사용하여 전체 스캔
name_x = ["Meredith", "Christina", "Alex", "George"]

# 1️⃣ 인덱스 값을 사용하지 않고 모든 요소 스캔 (자바의 향상된 for문과 같음)
for i in name_x :
    print(i)

# 2️⃣ 최종값만을 넣어서 원소 스캔 (리스트의 개수를 구해서 인덱스로 순회))
for i in range(len(name_x)) :
    print(name_x[i])

# 3️⃣ 다양한 자료형 및 중첩 리스트 접근
x = [4, 32, 7, 3.14, [32, 24], "hello"]
for i in range(len(x)) :
    print(f"x[{i}] = {x[i]}")


# 🔍 응용 문제 : 홀수, 짝수 나누어 담기
num_list = list(map(int, input("정수 입력 : ").split()))
print(num_list)
even_list = []
odd_list = []
for e in num_list : # number 리스트 요소로 자동 순회
    if e % 2 == 0 : even_list.append(e)
    else : odd_list.append(e)

print("짝수 : ", even_list)
print(f"홀수 : {odd_list}")

# 🔍 람다를 이용하는 방법
    # ✨ lambda 매개변수 : 표현식
    # ✨ filter(함수, 리스트) : 결과가 True인 것만 걸러냄
num_list = list(map(int, input("정수 입력 : ").split()))
odd_list = list(filter(lambda x: x % 2 == 1, num_list))
even_list = list(filter(lambda x: x % 2 == 0, num_list))

print(f"홀수 : {odd_list}")
print(f"짝수 : {even_list}")

    # 익명의 함수 사용 시 화살표 대신 lambda라고 명시적으로 입력
    # (X) => x % 2 == 1

