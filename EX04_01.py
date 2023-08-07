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
def add_many(*args): # *ars : 입력값을 전부 모아서 튜플로 만들어 준다,
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
    
"""