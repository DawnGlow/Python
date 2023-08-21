# 내장 함수 (Bulit-in-function)

"""
# abs 함수
- abs(x)
- 어떤 숫자를 입력받았을 때 그 숫자의 절댓값을 돌려주는 함수
ex)
abs(-3)
res : 3

# all 함수
- all(x) 
- 반복 가능한(iterable) 자료형 x를 인수로 받아 x가 모두 참이면 True, 거짓이 하나라도 있으면 False 돌려줌
ex) all([1, 2, 3])
res : True

# any 함수
- any(x)
- x 중 하나라도 참이 있으면 True, x가 모두 거짓일 때 False 돌려줌
ex) any([1, 2, 3, 0, 4])
res : True
ex) any([0, ""])
res : False

# char 함수
- chr(i)
- 아스키 코드값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
ex) chr(97)
res : 'a'
char(48)
res : '0'

# dir 함수
- 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
ex) dir([1, 2, 3])
['append', 'count', 'extend', 'index', ...]
ex) dir({'1': 'a'})
['clear', 'copy', 'get', 'has_key']

# divmod 함수
- divmod(a, b)
- 2개의 숫자를 입력받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
ex) divmod(7, 3)
res : (2, 1)

# enumerate 함수
- enumerate : '열거하다'
- 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 index 값을 포함하는 enumerate 객체로 리턴
ex)
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
res:
0 body
1 foo
2 bar

# eval 함수
- eval(expression)
- 실행 가능한 문자열(ex. 1+2, 'hi' + 'a') 을 입력 받아 문자열을 실행한 결괏값을 돌려주는 함수
- 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용
ex)
eval('1 + 2') # res : 3
eval("'hi' + 'a'") # res : 'hia'
eval('divmod(4, 3)') # res : (1, 1)

# filter 함수
- 첫번 째 인수로 함수이름, 두번째 인수로 함수에 차례로 들어갈 iterable 자료형을 받음
ex)
# positive.py
def positive(l):
    result = []
    for i in l:
        if (i > 0):
            result.append(i)
    return result

print(positive[1, -3, 2, 0, -5, 6])
결괏값 : [1, 2, 6]

위 함수를 fiilter 함수를 사용하여 다음과 같이 간단히 나타낼 수 있음
ex)
# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
--> filter 함수는 positive 함수에서 반환 값이 참인 것만 묶어서 돌려줌

ex) lambda 사용 # lambda 매개변수 : 표현식  
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))

# hex 함수
- hex(x)
- 정수값을 입력받아 16진수로 변환하여 돌려줌

# id 함수
- id(object)
- 객체를 입력받아 객체의 고유 주소(레퍼런스) 값을 돌려주는 함수
ex)
a = 3
id(3)
135072304
id(a)
135072304

# input 함수
- input([prompt])
- 사용자 입력을 받는 함수
- 매개변수로 문자열을 주면 프롬프트가 됨
ex) a = input()
ex) b = input("Enter: ")

# int 함수
- int(x)
- 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수형태로 돌려주는 함수
ex) int('3') # res : 3
ex) int(3.4) # res : 3
- int(x, radix)는 radix진수로 표현된 문자열 x를 10진수로 변환하여 돌려줌
ex) int('11', 2) # res : 3
ex) int('1A', 16) # res : 26

# isinstance 함수
- isinstance(object, class)
- 첫번 째 인수로 인스턴스, 두번 째 인수로 클래스
ex) class Person: pass
...
a = Person()
isinstance(a, Person) # res : True

# len 함수
- len(s)
- 입력값 s의 길이를 돌려주는 함수
ex) len("python") # res : 6
ex) len([1, 2, 3]) # res : 3
ex) len((1, 'a')) # res : 2

# list 함수
- list(s)
- 반복가능한 자료형 s를 입력받아 리스트로 만들어 주는 함수
ex) list("python") # res : ['p', 'y', 't', 'h', 'o', 'n']
ex) list((1, 2, 3)) # res : [1, 2, 3]
- 값만 복사(깊은 복사) 할 때도 사용
ex)
a = [1, 2, 3]
b = list(a)

# map 함수
- map(f, iterable)
- 함수 f와 반복 가능한(iterable) 자료형을 입력 받는다.
- 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려줌
ex)
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

위 코드를 map함수를 이용하여 다음처럼 바꿀 수 있다.
ex)
def two_times(x): return x * 2
...
list(map(two_times, [1, 2, 3, 4]))
- 1이 two_times 함수의 입력값으로 들어감
- 1 * 2가 되어 2가 됨.
- 모두 수행되면 [2, 4, 6, 8]
- 직접 인덱스에 접근해서 처리하는 것 보다 간결함.

ex) lambda 사용
list(map(lambda x: x*2, [1, 2, 3, 4]))

# max 함수
- max(iterable)
- 인수로 iterable 자료형을 받아 최댓값을 돌려주는 함수
ex)max([1, 2, 3]) # res : 3
ex)max("python") # res : 'y'

# min 함수
- min(iterable)
- 인수로 iterable 자료형을 받아 최솟값을 돌려주는 함수
ex)min("python") # res : 'h'

# oct 함수
- oct(x)
- 정수 형태의 숫자를 8진수 문자열로 바꿔주는 함수
ex) oct(34) # res : 0o42

# open 함수
- open(filename, [mode])
- 파일이름, 읽기방법을 입력받아 파일 객체를 돌려준다.
- 읽기방법 생략시 읽기전용모드(r)로 객체를 만들어 돌려줌
- w: 쓰기 모드, r: 읽기 모드, a: 추가 모드, b: 바이너리 모드 (w, r, a와 함께 사용)
ex) f = open("binary_file", "rb") # rb는 바이너리 읽기 모드

# ord 함수
- ord(c)
- 문자의 아스키 코드 값을 돌려주는 함수

# pow 함수
- pow(x, y)
- x의 y 제곱의 결괏값을 돌려줌

* pow(x, y)함수와 math.pow(x, y), x ** y와의 차이?
- math.pow(x, y)의 결괏값은 항상 float형
- pow는 3번째 파라미터로 나머지 계산 mod를 받을 수 있음. ex) pow(base, exp, mod) --> base, exp는 정수형
- base ** exp 는 속도가 셋 중에서 제일 빠름

# range 함수
- range([start,] stop[,step])
- for 문과 가장 많이 사용하는 함수
- 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려줌

* 인수가 하나일 경우
- 시작 숫자를 지정하지 않으면 range함수는 0부터 시작, 끝 숫자 포함 X
ex) list(range(5)) # res : [0, 1, 2, 3, 4]

* 인수가 2개일 경우
- 입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. 끝 숫자 포함 X
ex) list(range(5, 10)) # res : [5, 6, 7, 8, 9]

* 인수가 3개일 경우
- 세번 째 인수는 숫자 사이의 거리를 의미
ex) list(range(1, 10, 2)) # res : [1, 3, 5, 7, 9]
ex) list(range(0, -10, -1)) # res : [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
--> 0 부터 -9 까지, 정수 사이의 거리는 -1임

# round 함수
- round(number[, ndigits])
- 숫자를 입력받아 반올림 해주는 함수
ex) round(4.6) # res : 5
ex) round(5.678, 2) # res : 5.68
--> 소수점 [ndigits]자리까지 반올림하여 표시

# sorted 함수
- sorted(iterable)
- 입력값을 정렬한 후 결과를 리스트로 리턴
- list 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 하고, 리턴하지는 않음.
ex) sorted([3, 1, 2]) # res : [1, 2, 3]
ex) sorted(['a', 'c', 'b']) # res : ['a', 'b', 'c']
ex) sorted("zero") # res : ['e', 'o', 'r', 'z']
ex) sorted((3, 2, 1)) # res : [1, 2, 3]

# str 함수
- str(object)
- 문자열 형태로 객체를 변환하여 돌려주는 함수
ex) str(3) # res : '3'
ex) str('hi') # res : 'hi'
ex) str('hi'.upper()) # res : 'Hi'

# sum 함수
- sum(iterable)
- 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수(집합도 가능한 듯?)
ex) sum([1, 2, 3]) # res : 6
ex) sum((1, 2, 3)) # res : 6

# tuple 함수
- tuple(iterable)
- 반복 가능한 자료형을 입력받아 튜플형태로 돌려줌(튜플은 튜플 그대로 리턴)
ex) tuple("abc") # res : ('a', 'b', 'c')
ex) tuple([1, 2, 3]) # res : (1, 2, 3)
ex) tuple((1, 2, 3)) # res : (1, 2, 3)

# type 함수
- type(object)
- 입력값의 자료형이 무엇인지 알려주는 함수
ex) type(open("test", 'w')) # res : <class '_io.TextIOWrapper'>

# zip 함수
- zip(*iterable)
- 동일한 개수로 이루어진 자료형을 묶어줌
ex) list(zip([1, 2, 3], [4, 5, 6])) # res : [(1, 4), (2, 5), (3, 6)]
ex) list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])) # res : [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
ex) list(zip("abc", "def")) # res : [('a', 'd'), ('b', 'e'), ('c', 'f')]

"""