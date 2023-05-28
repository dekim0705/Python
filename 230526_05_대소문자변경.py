# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

result = ""
for e in input() : # input받은 갯수 만큼을 돌리기
    if e.islower() :
        result += e.upper()
    else :
        result += e.lower()
print(result)