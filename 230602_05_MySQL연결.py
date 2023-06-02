import pymysql

# 1️⃣ MySQL 연결하기
conn = pymysql.connect(host="127.0.0.1", user="root", password="0000", db="mysqlDB", charset="utf8")

# 2️⃣ 커서 생성하기
cur = conn.cursor()

# 3️⃣ 테이블 생성
cur.execute("CREATE TABLE userTable (id char(10), userName char(15), email char(20), birthYear int)")

# 4️⃣ 데이터 입력 하기
cur.execute("INSERT INTO userTable VALUES('userid1', '유저이름1', 'email1@gmail.com', 2003)")
cur.execute("INSERT INTO userTable VALUES('userid2', '유저이름2', 'email2@gmail.com', 2004)")

# 5️⃣ 데이터 저장하기
conn.commit()

# 6️⃣ 연결 종료하기
conn.close()



# 📌 데이터 입력 프로그램

# 전역 변수 
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드
conn = pymysql.connect(host="127.0.0.1", user="root", password="0000", db="mysqlDB", charset="utf8")
cur = conn.cursor()

while(True) :
    data1 = input("아이디 : ")
    if data1 == "" : break
    data2 = input("이름 : ")
    data3 = input("이메일 : ")
    data4 = input("출생연도 : ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', '" + data4 + "')"
    cur.execute(sql)

conn.commit()
conn.close()
