# 📌 JSON Encoding : Python Object(Dictionary, List Tuple 등)를 JSON 문자열로 변경하는 것
    # ✨ json.dumps()  : 인코딩 - JSON 문자열로 반환
    # ✨ json.loads()  : 디코딩 - JSON 문자열을 Python타입 (Dictionary, List, Tuple 등)으로 변경하는 것 
import json

customer = {    # {}는 딕셔너리 타입 ! 
    "id" : 123456,
    "name" : "홍길동",
    "history" : [
        {"date" : "2023-05-05", "제품" : "iPhone Pro 14"},
        {"date" : "2023-06-02", "제품" : "Galaxy S23"}
    ]
}

# 📌 JSON 인코딩
jsonString = json.dumps(customer, ensure_ascii=False) # ascii를 꺼줘야 한글지 깨지지 않음 
print(jsonString)

# 📌 JSON 디코딩
jsonString = '''{"name" : "KH", "id" : 123456, "history" : [
    {"date" : "2023-05-10", "item" : "iPhone 14 Pro"},
    {"date" : "2023-05-24", "item" : "Galuxy S23 Ultra"}
]}'''

dic = json.loads(jsonString)
print(dic)
# print(dict["name"])
# for h in dict["history"] : 
#     print(h["date"], h["item"])
