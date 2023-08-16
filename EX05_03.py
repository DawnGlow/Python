# 패키지

"""
# 패키지란 무엇인가?

- 패키지는 도트를 사용하여 파이썬 모듈을 계층적(디렉토리 구조)으로 관리할 수 있게 해줌
- 모듈이름이 A.B인 경우에 A는 패키지 이름, B는 A 패키지의 모듈이 된다.

ex)
game/
  __init__.py
  sound/
    __init__.py
    echo.py
    wave.py
  graphic/
    __init__.py
    screen.py
    render.py
  play/
    __init__.py
    run.py
    test.py

- 패키지 구조로 파이썬 프로그램을 만들면 공동작업이나 유지보수 등 여려면에서 유리
- 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용 가능

# 패키지 만들기

* 패키지 기본 구성 요소 준비
* 패키지 안의 함수 실행하기
ex1)
import game.sound.echo
game.sound.echo.echo_test()
ex2)
from game.sound import echo
echo.echo_test()
ex3)
from game.sound.echo import echo_test()
echo_test()

* 다음과 같은 상황은 에러 발생
ex4)import game
game.sound.echo.echo_test() # 에러 발생
- game 디렉토리의 모듈 또는 game 디렉토리의 __init.py__만 참조할 수 있다.
ex5)
import game.sound.echo.echo_test # 에러발생
- import에서 a.b.c의 항목 c는 반드시 모듈 또는 패키지여야만 한다.

# __init__.py의 용도

- 해당 디렉토리가 패키지의 일부임을 알려줌
- __init__.py가 없으면 패키지로 인식하지 않는다.

ex)
from game.sound import *
echo.echo_test() # 에러발생
- 에러가 발생한 이유 : __init__.py 파일에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해야 한다.
__all__ = ['echo', '추가로 더있다면 추가']


# relative 패키지

ex) grpahic 패키지의 render.py모듈이 sound디렉토리의 echo.py 모듈을 사용하고 싶은 경우
# render.py
from game.sound.echo import echo_test 추가 후 render.py에서 echo.py 모듈사용

* 조금 더 relative하게 import 해보고 싶다
- ..(relative한 접근자) 사용 : 부모 디렉터리 의미
- graphic과 sound의 디렉토리의 depth가 같으므로 가능한 것
- 모듈안에서만 사용해야 하고, 인터프리터에서는 절대 사용 X(에러 발생)
ex) from ..sound.echo import echo_test


"""