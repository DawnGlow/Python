# while문

"""

# while문의 기본 구조
- 조건문이 참인 동안 문장을 반복해서 실행
while 조건문:
    수행할 문장1
    수행할 문장2
    ...

ex)
treeHit = 0 # 나무를 찍은 횟수
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

# while문 강제로 빠져 나가기
break 사용 --> while문 탈출
ex)
coffee = 10
money = 5000
while money >= 300:
    money -= 300
    if coffee == 0:
        print("커피가 다 떨어졌습니다")
        break
    else:
        print("돈을 지불했으니 커피를 줍니다")
        coffee -= 1
        print(f'앞으로 커피를 {coffee}잔 뽑을 수 있습니다.')

# while문 맨 처음으로 돌아가기
continue 사용 --> while문 맨 처음으로

ex) 
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)

Exercise)
a = 0
while a < 10:
    a += 1
    if (a % 3 == 0): continue
    print(a)

"""