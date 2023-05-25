# 규칙1 : http://naver.com에서 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점(.) 이후는 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o' 갯수 + 글자에 포함된 'k' 갯수 + '!' + 자신의 이니셜(예: 'jks')

file_name = "password.txt"
f = open(file_name, "wt") # write
while True: 
    url = input("사이트 : ")
    if url == "exit" : break # 종료 조건
    my_str = url.replace("http://", "") # http:// 잘라내서 버림
    my_str = my_str[:my_str.index(".")] # 0번 인덱스 부터 .위치 미만
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("n")) + "!" + "pwd"
            # 처음부터 3번 인덱스 까지 자르기 + 전체 길이 + n이 포함된 갯수 + ! + pwd
    f.write(password + "\n")
f.close() # 파일 닫기 