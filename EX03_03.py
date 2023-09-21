# for문

"""
# for문의 기본 구조

for 변수 in 리스트(또는 튜플, 문자열):
    수행문장
    ...

ex)
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


ex)
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(f'({first}, {last})')

ex)
marks = [70, 30, 100, 65, 59]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print(f'{number}번째 학생의 점수는 {mark}점이므로 합격입니다')
    else:
        print(f'{number}번째 학생의 점수는 {mark}점이므로 불합격입니다')

# for문에서 continue문 사용

ex)
marks = [70, 30, 100, 65, 59]
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue
    print(f'{number}번째 학생의 점수는 {mark}점이므로 합격입니다')

# for문에서 자주 사용하는 range함수

a = range(10)
a
res : range(0, 10) # 0부터 10 미만의 숫자를 포함하는 range 객체

# enumerate 함수
ex) for (idx, data) in enumerate(iterable)
--> index와 iterable 변수를 묶음

ex)
add = 0
for i in range(1, 11):
    add += i

print(add)
res : 55

* for와 range를 이용해 구구단 출력하기
- print함수의 매개변수에 end=" "를 사용하면, 같은줄에 " "출력 후 다음 값을 출력한다.
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print('')

# 리스트 내포 사용하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

위 코드를 리스트 내포를 사용해 아래처럼 사용할 수 있다.

a = [1, 2, 3, 4]
result = [num * 3 for in a]

만약 짝수에만 3을 곱하고 싶으면
result = [num * 3 for in a if num % 2 == 0] 으로 사용

형식을 정리하자면
[표현식 for 항목 in 반복 가능 객체 if 조건]

2개 이상의 for문도 가능하다.
[표현식 for 항목1 in 반복가능객체 if 조건 1
    for 항목 2 in 반복가능객체 if 조건 2
    for ...]
ex) 구구단
result = [x * y for x in range(1, 10)
    for y in range(1, 10)]


"""