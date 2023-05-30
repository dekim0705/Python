# 📌 집합(set) : 순서가 없고, 고유한 값을 가지며 중복 불가능, mutable 특성
    # ✨ 주로 다른 자료형의 중복 제거 할 때 자주 사용


# 📌 중복 제거
s1 = set([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])
print('중복 제거 : ', s1)


# 📌 교집합 : 양쪽에 모두 존재하는 요소만 선택
s2 = set([1,2,3,4,5])
s3 = set([1,3,7,6,8,9])
print('교집합 : ', s2.intersection(s3))


# 📌 합집합
print('합집합 : ', s2.union(s3))


# 📌 차집합 (앞에서 뒤를 빼는 것)
print('차집합 : ', s2.difference(s3))


# 🔍 중복 제거로 로또 번호 만들기
import random
lotto = set()
while True :  # while문 굳이 돌릴 필요 X
    num = random.randrange(1, 46)
    lotto.add(num)
    if len(lotto) == 6 : break
print(lotto)

