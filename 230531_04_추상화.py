# 📌 부모 클래스에서 추상 메소드로 선언한 메소드에 대해서는 반드시 상속 받은 자식 클래스에서 해당 기능을 구현 해야 함

from abc import *

class NetworkAdapter(metaclass=ABCMeta) : # 자바에서 abstract 붙이는 것과 동일
    @abstractmethod
    def connect(self) :
        pass

class FiveG(NetworkAdapter) : # NetworkAdapter 상속
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} 5G로 연결 하였습니다.")

class WiFi(NetworkAdapter) : # NetworkAdapter 상속
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} Wi-Fi로 연결 하였습니다.")

class LTE(NetworkAdapter) : # NetworkAdapter 상속
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} LTE로 연결 하였습니다.")

net = input("연결할 네트워크를 선택 하세요 : [1]5G, [2]Wi-Fi, [3]LTE : ")
if net == "1" :
    adapter = FiveG("KT Megapass")
    adapter.connect()
elif net == "2" :
    adapter = WiFi("SK Telecom")
    adapter.connect()
elif net == "3" :
    adapter = LTE("LG U+")
    adapter.connect()
else : print("연결할 네트워크가 없습니다.")