# if문

"""
# if문의 기본구조

if 조건문:
    수행할 문장 1
    수행할 문장 2

else:
    수행할 문장 A
    수행할 문장 B
    
- 들여쓰기를 할 때 공백 4개, 탭 중 하나만 선택해서 사용하자.(혼용할 시 에러 발생)
- 조건문 다음에 반드시 콜론을 붙히자.

# 조건문이란?

* 비교 연산자
c와 동일. bool 값을 반환한다.

* and, or, not
x or y // x와 y 둘 중 하나만 참이여도 참
x and y // x와 y 둘다 참이어야 참
not x // x가 거짓이면 참

* x in s, x not in s
x in 리스트, x in 튜플, x in 문자열
ex)
1 in [1, 2, 3]
res : true
'j' not in 'python'
res : true

ex)
pocket = ['card', 'money', 'phone']
if 'card' not in pocket:
    print("걸어가세요")
else:
    print("버스를 타세요")

* 조건문에서 아무 일도 하지 않게 하려면?
- 수행할 문장 대신에 pass를 사용한다.

* elif(c의 else if)
- 여러 조건을 판별할 때 사용
if 조건문:
    수행문장 1-1
    수행문장 1-2
elif 조건문:
    수행문장 2-1
    수행문장 2-2
elif 조건문:
    수행문장 3-1
    수행문장 3-2
else:
    수행문장 4-1
    수행문장 4-2

* if문 한줄로 작성하기
if 'money' in pocket: pass
else: print("카드를 꺼내라")


# 조건부 표현식

if score >= 60:
    message = "success"
else:
    message = "failure"

위 코드를 조건부 표현식을 이용하여

message = "success" if score >= 60 else "failure"
로 표현 가능하다.

(참 수행문장) (if 조건문) (else 거짓 수행문장)
"""