# 요금제 계산
# 영식 요금제 : 30초에 10원
# 민식 요금제  : 60초에 15원
# 입력은 첫 줄에 통화 횟수를 입력 받고 다음줄에 각 통화에 대한 통화 시간을 입력 받음
# 3
# 34 56 78

cnt = int(input("통화 횟수"))
call_time = list(map(int, input("통화 시간 : ").split()))
y_pay = m_pay = 0

for i in range(cnt) :
    y_pay += (call_time[i] // 30) * 10 + 10 
    # 30초에 10원이니까 30으로 나눈 몫을 구해야 함. 한 통화마다 10원이니까 *10. 
    m_pay += (call_time[i] // 60) * 15 + 15
if y_pay > m_pay :
    print("M", m_pay)
elif y_pay < m_pay :
    print("Y", y_pay)
else :
    print("Y M", y_pay)