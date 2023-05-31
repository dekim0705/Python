# 📌 객체지향 프로그램의 특성
    # ✨ 상속   : 이미 만들어져있는 것을 가지고 와서 사용할 때 부모로부터 물려받아서 사용
    # ✨ 캡슐화 : 외부에서 내부값에 접근할 수 없도록 값을 보호하는 것 (게터와 세터 사용)
    # ✨ 다형성 : 상속이 선행되어야 하고, 상속받은 것을 modify, 재정의 하는 것 (오버로딩(파이썬에는 X), 오버라이딩))
    # ✨ 추상화 : 객체화가 되지 않는 부모로부터 특성을 물려받는 경우 


# 🔍 TV 만들기 및 생성자
    # 생성자 : 클래스가 객체로 만들어 질 때 자동으로 호출되며, 객체의 초기값을 지정 할 수 있음
    # 생성자 키워드 : __init__
    # self : 자신의 객체를 가리키는 포인터 (내부의 값을 초기화)

class TV :
    def __init__ (self, name, is_on, channel, volume) :
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on) :
        self.is_on = is_on
    def set_channel(self, cnl) : 
        self.channel = cnl
    def set_volume(self, vol) :
        self.volume = vol
    def get_on(self) :
        return self.is_on
    def get_channel(self) :
        return self.channel
    def get_volume(self) :
        return self.volume
    def view_tv(self) :
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}") # 파이썬은 참과거짓을 0과 1로 구분
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = TV("LG", False, 10, 10)
samsung_tv = TV("SAMSUNG", False, 20, 20)

samsung_tv.view_tv()
lg_tv.view_tv()

lg_tv.set_on(True)
lg_tv.set_volume(28)
lg_tv.set_channel(1)
lg_tv.view_tv()





