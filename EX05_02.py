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

"""