# 함수


"""
# 파이썬 함수의 구조
def 함수 이름(매개변수):
    수행할 문장 1
    수행할 문장 2
ex)
def add(a, b):
    return a + b
a = 3
b = 4
print(add(a, b))

* 매개변수가 없을 수도 있다.
* 결괏값이 없는 함수도 있다.
ex)
def add(a, b):
    print(f'{a} + {b} = {a + b}')

이때 add 함수는 반환값이 없다.(a = add(3,4) 를 출력했을 때 none이라고 나왔다고 반환값이 있다고 생각하면 안된다!)

# 매개변수 지정하여 호출하기
def add(a, b):
    return a + b
result = add(a = 3, b = 7)
result = add(b = 5, a = 3)

이런식으로 매개변수를 지정할 수 있다.

# 입력값이 몇 개가 될지 모를 때
* 매개변수로 *args 단독
def 함수이름(*매개변수):
    수행할 문장
    ...
ex)
def add_many(*args): # *args : 입력값을 전부 모아서 튜플로 만들어 준다,
    result = 0
    for i in args:
        result += i
    return result

* 매개변수로 *args 외 다른 것과 같이 쓸 때
ex)
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            reuslt += i
    return result
    
# 키워드 파라미터

- 매개변수 앞에 ** 사용 : 매개변수가 딕셔너리로 만들어져 출력됨.
ex) 
def print_kwargs(**kwargs):
    print(kwargs)

>>> print_kwargs(a=1)
res: {'a': 1}

# 함수의 결과값은 언제나 하나이다

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3,4)
--> result = (7, 12)
리턴값이 2개가 아니라, (a+b, a*b) 라는 튜플 값을 결과 값으로 받는다.

두개의 결과값처럼 받고 싶다면
result1, result2 = add_and_mul(3, 4)
로 호출하면 된다.
이러면 result1, result2 = (7, 12) 이므로 result1 = 7, result2 = 12가 된다.

* 특별한 상황일 때 함수를 빠져나가기
--> return 사용
ex)
def say_nick(nick):
    if nick == "바보":
        return # 함수 탈출
    print(f'나의 별명은 {nick}입니다')

# 매개변수에 초깃값 미리 설정하기 (cpp랑 비슷)
ex)
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
--> name에는 "박응용", old에는 27, man은 입력값이 없으므로 초깃값인 True를 갖는다.
say_myself("박응용", 27, False)
--> name에는 "박응용", old에는 27, man은 False이므로 "여자입니다"가 출력된다.

다음과 같이 초깃값을 설정하면 안된다.
def say_myself(name, man=True, old):
--> 오른쪽부터 초깃값을 설정해야 한다.

# 함수안에서 선언한 변수의 효력 범위

결론 : 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다.

* 함수 안에서 함수 밖의 변수를 변경하는 방법
1. return 사용하기
ex)
"""
a = 1
def vartest(a):
    a += 1
    return a
a = vartest(a)
print(a)

"""
2. global 명령어 사용하기
ex)
"""
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)

"""
- global 명령어를 함수 안에서 사용하는 것은 별로 좋지 않음.
- 함수는 독립적으로 존재하는게 좋고, 외부 변수에 종속적인 함수는 좋은 함수가 아니다.

# lambda

- lambda는 함수는 생성할 때 사용하는 예약어
- def와 동일한 역할
- 함수를 한줄로 간결하게 만들 때 사용
- def를 사용할 정도로 복잡하지 않거나, def를 사용할 수 없을 때 사용

- 형식
lambda 매개변수1, 매개변수2, .... : 매개변수를 사용한 표현식
ex)
"""
add = lambda a, b: a + b # 리턴 명령어가 없어도 결괏값을 돌려줌
result = add(3, 4)
print(result)


