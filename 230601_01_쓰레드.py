# 📌 쓰레드 : 하나의 프로세스 내에서 독립적으로 실행될 수 있는 작은 실행 단위
from simple_colors import *  # 화면 출력에 컬러 넣기
import threading
import time
import random

class Unit:
    def __init__(self, pp, mp, ph, mh, hp):
        self.pPower = pp
        self.mPower = mp
        self.pHit = ph
        self.mHit = mh
        self.hp = hp
        self.isAlive = True

class Charactor(Unit):
    def __init__(self, pp, mp, ph, mh, hp, um, job):
        Unit.__init__(self, pp, mp, ph, mh, hp)
        self.ultimate= um  # 궁극기 특성 추가
        self.job = job
    def p_attack(self):
        return self.pPower * self.pHit
    def m_attack(self):
        return self.mPower * self.mHit
    def attack_ultra(self):
        return self.ultimate
    def is_alive(self):
        return self.isAlive
    def setDamage(self, damage):
        if self.hp > damage:
            self.hp -= damage
            print(f"남아 있는 {green(self.job)}의 체력은 {blue(self.hp)} 입니다.")
            self.isAlive = True
        else:
            print(f"{green(self.job)}가 죽었습니다. 게임을 종료 합니다.")
            self.isAlive = False

 
# 스레드에서 실행할 함수
def wizard_th(dummy):
    print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    while True :
        time.sleep(5)
        if warrior.is_alive() == False or wizard.is_alive() == False :
            break
        val = random.randrange(0,2)
        ul = random.randrange(0, 18)
        if val == 0:
            print(f"{blue('물리공격')} >> {warrior.job}에게 {yellow(wizard.p_attack())} 데미지를 입혔습니다.")
            warrior.setDamage(wizard.p_attack())
        else:
            print(f"{yellow('마법공격')} >> {warrior.job}에게 {yellow(wizard.m_attack())} 데미지를 입혔습니다.")
            warrior.setDamage(wizard.m_attack())
        if ul == 1 :
            print(f"{red('궁극기 발동')} >> {warrior.job}에게 {red(wizard.attack_ultra())} 데미지를 입혔습니다.")
            warrior.setDamage(wizard.attack_ultra())

 
# 메인 영역
if __name__ == "__main__": # main thread 흐름을 타는 시작점

    name1 = input("전사는 강력한 체력의 물리공격형 캐릭터 (이름 입력) : ")
    name2 = input("마법사는 강력한 마법 공격형 캐릭터 (이름 입력) :  ")

    warrior = Charactor(8, 2, 0.8, 0.5, 150, 40, name1) # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기
    wizard = Charactor(2, 20, 0.5, 0.9, 60, 55, name2) # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기
    x = threading.Thread(target=wizard_th, args=(1,)) 
    print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    x.start() # 서브 스레드 시작
    while True :
        time.sleep(5)
        if warrior.is_alive() == False or wizard.is_alive() == False :
            break
        val = random.randrange(0,2)
        ul = random.randrange(0, 12)
        if val == 0:
            print(f"{blue('물리공격')} >> {wizard.job}에게 {warrior.p_attack()} 데미지를 입혔습니다.")
            wizard.setDamage(warrior.p_attack())
        else:
            print(f"{yellow('마법공격')} >> {wizard.job}에게 {warrior.m_attack()} 데미지를 입혔습니다.")
            wizard.setDamage(warrior.m_attack())
        if ul == 1 :
            print(f"{red('궁극기 발동')} >> {wizard.job}에게 {red(warrior.attack_ultra())} 데미지를 입혔습니다.")
            wizard.setDamage(warrior.attack_ultra())