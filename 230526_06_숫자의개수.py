# 세개의 자연수를 입력받아서 모두 곱하고
# 결과값에서 나오는 숫자의 횟수를 출력하기
# 17037300 => 0은 3, 1은 1, 7은 2번

a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = list(str(a * b * c))
# ls = str(a * b * c)   # list빼도 돌아감 
# print(ls) # ['1', '7', '0', '3', '7', '3', '0', '0']
for i in range(10) :
    print(ls.count(str(i))) 
