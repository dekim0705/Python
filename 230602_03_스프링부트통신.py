import requests
import json

data = {
    "id" : "홍길동1234",
    "pwd" : "pwd1234"
}

# JSON 데이터를 서버로 전달
url = "http://localhost:8111/login"
header = {"Content-Type" : "application/json"}

response = requests.post(url, data=json.dumps(data), headers=header)

# 서버 응답 확인
if response.status_code == 200 :
    print("데이터가 성공적으로 전송되었습니다.")
else : 
    print("데이터 전송에 실패했습니다. 응답 코드 : ", response.status_code)
