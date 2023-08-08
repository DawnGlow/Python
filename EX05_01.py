# 클래스

"""

# 클래스와 객체
과자 틀 -> 클래스
틀을 이용해 만든 과자 -> 객체

* 객체와 인스턴스의 차이
a = Cookie() 에서 a는객체, a 객체는 Cookie의 인스턴스이다.
인스턴스 : 특정 객체가 어떤 클래스의 객체인지 관계 위주로 설명할 때 사용하는 말

# 사칙 연산 클래스 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first # a.first = first, a 객체에 객체변수 first가 생성되고 값 4 가 저장된다.
        self.second = second # a.second = second, a 객체에 객체변수 second가 생성되고 값 2가 저장된다.
    def add(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

* self란 무엇인가?
- 클래스의 메서드를 호출하면 메서드의 첫번째 매개변수 self에는 메서드를 호출한 객체가 자동으로 전달된다.
- 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.(다른 이름을 사용해도 상관 없음)

* 메서드의 또 다른 호출 방법
- 클래스를 통해 메서드를 호출할 수 있다.
ex)
a = FourCal()
FourCal.setdata(a, 4, 2)
---> 클래스이름.메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수에 꼭 전달 해줘야 한다!
---> 객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 한다.

# 생성자(Constructor)

만약 계산기 클래스에서
a = FourCal()
a.add()
이렇게 실수를 해버리면 오류가 발생한다.(setdata를 수행해야 객체변수가 생기기 때문)
setdata 메서드를 호출하는 것 보다 생성자를 구현하는 것이 안전

- 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드를 의미.
- 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다.

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

이 상태에서 a = FourCal()을 수행하면 매개변수가 없어 오류가 발생한다.


# 클래스의 상속

- 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받는 것

형식:
class 클래스 이름(상속할 클래스 이름):

- 상속을 하는 이유?
--> 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않으면 상속해서 사용할 수 있음

ex) a의 b제곱 기능을 포함하는 계산기

class MoreFourCal(Fourcal):
    def pow(self):
        return self.first ** self.second


* 메서드 오버라이딩
- 부모 클래스에 있는 메서드를 동일한 이름으로 다시 작성(오버라이딩, 덮어쓰기) 하는 것

a = FourCal(4, 0)
a.div()를 실행하면 0으로 정수를 나누기 때문에 오류가 발생한다.
이를 해결하고자 FourCal 클래스를 상속하는 SafeFourCal 클래스를 만들자

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0
            return 0
        else:
            return self.first / self.second

# 클래스 변수

- 객체변수들은 다른 객체들에 영향을 받지 않고 독립적으로 그 값을 유지함
- 클래스 변수는 함수를 선언하는 것처럼 클래스 안에서 변수를 선언하여 생성한다.
- 어느 객체에서나 동일한 클래스 변수를 가진다.
- 객체.클래스변수로 값을 변경하면 다른 객체에서의 값도 다 변경된다.(모든 객체에 공유된다.)
- 모든 객체에서 공유하고 있기 때문에 어느 인스턴스에서 접근하든 주소 또한 동일하다.
ex)
class Family:
    lastname = "김" # 클래스 변수

a = Family()
b = Family()

Family.lastname = "park"
--> 클래스 변수값이 변경되어 a, b 객체에서도 lastname이 "park"로 변경된다

!!! a.lastname 이나 b.lastname으로 접근하면 이는 클래스 변수가 아닌 객체 변수에 접근하는 것임을 주의하자. !!!
"""