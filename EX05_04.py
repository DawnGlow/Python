# 예외처리

"""
# 오류가 발생하는 경우
ex) 0으로 나누는 경우
ex) 없는 파일을 'r' 모드로 읽으려고 하는 경우

# 오류 예외 처리 기법

* try.except문
- try 블록 수행 중 오류가 발생하면, except블록 실행.
- try 블록 수행 중 오류가 발생하지 않으면, except 블록 실행 X

except [발생 오류 [as 오류 메시지 변수]]:

- []기호는 괄호 안의 내용을 생략할 수 있다는 관례 표시

* except 구문을 사용하는 3가지 방법
1. try, except 만 사용
try:
    ....
except:
    ....

2. 발생 오류만 초함한 except문
try:
    ....
except 발생오류:
    ....

3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
    ....
except 발생 오류 as 오류 메시지 변수:
    ....

ex)
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

ex)
a = [1, 2]
try:
    a[3]
except IndexError as e:
    print(e)

    
* try ... finally
- try문에는 finally 절을 사용할 수 있음
- finally문은 예외 발생 여부 상관없이 항상 수행
- 리소스를 close할 때 많이 사용 (아래 예시처럼)

ex)
f = open('foo.txt', 'w')
try:
    # 무언가를 수행
finally:
    f.close()

    
* 여러개의 오류 처리하기
try:
    ....
except 발생오류 1:
    ....
except 발생오류 2:
    ....

ex)
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("Can't Divide by Zero.")
except IndexError:
    print("Can't Indexing.")
--> 인덱싱 오류가 먼저 발생하므로 ZeroDivisionError에 해당하는 오류가 발생하지 않음

ex)
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

ex)
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
--> 2개 이상의 오류를 동시에 처리하기 위해서는 위와 같이 괄호를 사용하여 묶어 처리한다.


# 오류 일부러 발생시키기
- raise 명령어 사용

ex)
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly() # NotImplemented Error 발생

# 예외 만들기
- 특수한 경우에만 예외 처리를 하기 위해 예외를 만들어서 사용하기도 함

ex) 파이썬 내장 클래스 Exception 클래스
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("바보") # 오류 발생

ex) 위 예시에서 예외처리 기법 사용
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

res :
천사
허용되지 않는 별명입니다.

ex)
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e) # 오류 메시지가 출력되지 않음

--> Exception 클래스를 상속받은 MyError 클래스가 어떤 오류인지 모름
--> print(e)로 오류메시지를 보이게 하려면 오류 클래스에 __str__ 메서드를 구현해야 함.
ex)
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

"""