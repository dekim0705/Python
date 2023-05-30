# 🔍 입력 받은 수가 소수인지 아닌지 판별하기 (함수 이용)
    # 소수란? 1과 자기 자신 이외에 나누어지지 않는 수

# def check_prime(n) :
#     if n == 1 : return False
#     for i in range(2, n) :
#         if n % i == 0 : return False
#         return True

# n = int(input("정수 입력 : "))
# print(f"소수 : {check_prime(n)}")

def is_prime(n) :
    for i in range(2, n) :  # 2부터 n 미만까지 : 1과 자기 자신 제외
        if n % i == 0 : return False
    return True

n = int(input("정수 입력 : "))
if (is_prime(n)) : print(f"{n}은 소수 입니다.")
else : print(f"{n}은 소수가 아닙니다.")
