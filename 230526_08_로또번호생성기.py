# 🔍 중복값이 없는 로또 번호 생성

import random
print("로또 번호 자동 생성 : ", end="")
ls = [] # empty list
while True :
    rand = random.randrange(1, 46)
    if rand not in ls : # list내에 포함되어있지 않으면 append~ 
        ls.append(rand)
    if len(ls) == 6 : break
print(ls)

