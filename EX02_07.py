# 불 자료형 (bool)

"""
# 불 자료형이란

- bool 자료형은 True, False 만 값으로 가짐(무조건 대문자로!!)
a = True
type(a)
res : <class 'bool'>
- 조건문의 반환 값으로도 사용된다.
ex) 1 == 1 res : true

# 자료형의 참과 거짓

- 문자열, 리스트, 튜플, 딕셔너리의 값이 비어있으면([], (), {}, "") 거짓
- 숫자형 0은 거짓
- 나머지는 전부 True
- None은 False
사용 예시) while문
a = [1, 2, 3, 4]
while a:
    a.pop()

4
3
2
1

--> pop을 하면서 a가 []가 되면 false 가 되므로 반복문이 중단되는 것이다.

if [1, 2, 3]:
    print("참")
else:
    print("거짓")

# 불 연산

bool('python')
res : True
bool('')
res : False
bool(0)
res : false
"""