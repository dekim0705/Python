# 📖 배수 찾기
# 문제 : 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때, 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램을 작성하시오.
# 출력 : 목록에 있는 수가 n의 배수인지 아닌지를 구한 뒤 예제 출력처럼 출력한다.

# ❗️ 예제 입력
# 3
# 1
# 7
# 99
# 321
# 777
# 0

# ❗️ 예제 출력
# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.


# 1️⃣ 정수 n을 입력 받음
# 2️⃣ 목록을 저장할 빈 리스트 생성
# 3️⃣ 무한의 반복문을 수행하면서 목록을 입력 받고 0이 입력되면 빠져 나감
# 4️⃣ 입력받은 목록을 순회하면서 목록의 값과 주어진 n값이 배수인지 비교해서 출력

n = int(input())
ls = []
while True :
    x = int(input())
    if x == 0 : break
    ls.append(x)

for e in ls :
    if e % n == 0 : print(f"{e} is a multiple of {n}.")
    else : print(f"{e} is NOT a multiple of {n}.")