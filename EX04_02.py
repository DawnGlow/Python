# 사용자 입력과 출력

"""
# 사용자 입력

* input 사용
a = input()
내용 입력 # 사용자가 입력한 문장을 a에 대입
a
res : 내용 입력

* 프롬프트 값을 띄워서 사용자 입력 받기
- input()의 괄호 안에 문자열을 입력하여 프롬프트를 띄우면 된다.
ex)
number = input("숫자를 입력하세요: ")

# print 자세히 알기

* 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다.
print("Life" "is" "too short")는
print("Life" + "is" + "too short")와 동일하다.

* 문자열 띄워쓰기는 콤마로 한다.
print("Life", "is", "too short")

* 한줄에 결괏값 출력하기
- 매개변수 end를 사용해 끝 문자를 지정한다.
for i in range(10):
    print(i, end=' ')
"""