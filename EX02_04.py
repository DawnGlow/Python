# 튜플 자료형

"""
* 리스트와 튜플의 공통점, 차이점
1. 리스트는 []로 둘러싸고, 튜플은 ()로 둘러쌈
2. 리스트는 값의 생성, 수정, 삭제가 가능하지만, 튜플은 그 값을 바꿀 수 없다. (실행 시 오류 발생)
--> 값이 바뀔 까 걱정될 때는 튜플을, 값이 자주 변화될 경우에는 리스트를 사용한다.
ex)
t1 = ()
t2 = (1,) # 1개의 요소만을 가질 때는 요소 뒤에 ,를 붙여야 한다.
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 괄호를 생략해도 무방하다
t5 = ('a', 'b', ('ab', 'cd'))

* 튜플 인덱싱 : 튜플이름[인덱스]
t1 = (1, 2, 'a', 'b')
t1[0]
res : 1

* 튜플 슬라이싱 : 리스트랑 비슷
t1 = (1, 2, 'a', 'b')
t1[1:] # 대괄호를 사용하자
res : (2, 'a', 'b')

* 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2
res : (1, 2, 'a', 'b', 3, 4)

* 튜플 곱하기(반복)
t2 = (3, 4)
t2 * 3
res : (3, 4, 3, 4, 3, 4)

* 튜플 길이 구하기(len 함수)
t1 = (1, 2, 'a', 'b')
len(t1)
res : 4

* (1, 2, 3)에 값 4를 더해 (1, 2, 3, 4) 만들기
(1, 2, 3) + (4,)

* extended unpacking
prof_tuple = ('choi', 327, True)
name, *others = prof_tuple
# name = 'choi'
# others = (327, True)

"""