# 모듈

"""
# 모듈이란?
- 함수나 변수 또는 클래스를 모아 놓은 파일
- 다른 파이썬 프로그램에서 불러와 사용할 수 있게 만든 파일이기도 하다.
- 이미 만들어 놓은 모듈을 사용할 수도 있고, 직접 만들 수도 있다.

# 모듈 만들기
ex) mod1.py에 덧셈, 뺄샘 함수를 만들었는데, 이 파일을 모듈이라 할 수 있다.

# 모듈 불러오기
* import
- 대화형 인터프리터 사용 시 디렉토리를 모듈 파일이 존재하는 곳으로 이동시켜야만 import 할 수 있음.
- 형식 : import 모듈이름 (.py 쓰면 안됨!!)
ex)
import mod1
print(mod1.add(3,4))
res : 7
print(mod1.sub(3,4))
res : -1

- 실수로 import mod1.py라고 하면 안된다.
- 모듈에 있는 함수를 사용할 땐 (모듈이름).(함수이름) 를 사용하자

* from 모듈 import 함수
- 모듈 이름 없이 함수 이름만 쓰고 싶은 경우 
from '모듈이름' import '모듈함수' 사용
ex) 
from mod1 import add

* 2가지 이상 함수를 import 하고 싶을 때는?
1. from mod1 import add, sub
- 콤마로 구분하여 필요한 함수를 불러올 수 있음
2. from mod1 import *
- *문자(모든것을 의미) 사용 --> mod1의 모든 함수 사용

# if __name__ == "__main__":의 의미
- 모듈로 불러서 사용할 때는 false가 됨
- 파일을 직접 실행할 때는 true가 됨.
- 어떤 ex.py를 import하면, false가 되고, python3 ex.py로 실행하면 true가 된다.
- 모듈로 import 할 때 실행될 필요가 없는 부분을 if __name__ == "__main__"로 처리하면 된다.

* __name__변수
- ex.py라는 함수를 직접 실행하면 __name__변수에는 __main__ 이 저장된다.
- 파이썬 셸이나 모듈에서 ex.py를 import하면 __name__변수에는 ex.py가 저장된다.


# 클래스나 변수 등을 포함한 모듈

- 변수 접근 : 모듈이름.변수이름
ex)mod2.py를 import 하고 print(mod2.PI)실행
res : 3.141592

- 모듈에 있는 클래스 생성 : 모듈이름.클래스() # 모듈이름 표기!
ex)
a = mod2.Math()

- 모듈에 있는 클래스의 메서드 접근 : 변수이름.메서드이름(매개변수) # 모듈이름은 따로 표기하지 않는다.
ex)
a.solv(2)

- 함수 호출 : 모듈.함수이름(매개변수)
ex)mod2.add(mod2.PI, 4.4)

* exercise) 반지름이 5인 원의 넓이
b = mod2.Math()
b.solv(5)

* 환경변수나 sys.path모듈을 이용하여 모듈을 이동시키지 않고 import 할 수 있다.
"""