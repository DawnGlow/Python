# 문자열을 만드는 방법
#1. 큰따옴표로 둘러싸기
#2. 작은따옴로 둘러싸기
#3. 큰따옴표 3개를 연속으로 둘러싸기
#4. 작은따옴표 3개를 연속으로 둘러싸기
say = "Hello World"
say = 'Python is fun'
say = 'test3'
say = 'test4'
'''
문자열에 작은따옴표 넣을땐 큰따옴표로 싸고, 반대도 마찬가지
다른방법
백슬래시를 '나 "앞에 넣는다.
'''
#여러줄의 문자열을 변수에 대입하는법
#1 (줄이 길어지는 단점이 있음)
multiline = "Life is too short\nYou need python"
#2
multiline = '''
Life is too sort
You need python
'''
print(multiline)
#3
multiline = """
Life is too short
You need python
"""
print(multiline)
'''
개행문자
\n : 줄바꿈
\t : 탭
\\ : \표현
\' : 위에서
\" : 위에서
\r : 캐리지 리턴(줄바꿈 문자, 현재 커서를 가장 앞으로)
\f : 폼 피드(줄바꿈 문자, 현재 커서를 다음줄로)
\a : 벨소리
\b : 백스페이스
\000 : 널문자
'''

#문자열 더하기
head = "python"
tail = "is fun"
print(head + tail)

#문자열 곱하기
a = "python"
print(a * 2)

#문자열 곱하기 예시
print("=" * 50)
print("example")
print("=" * 50 + "\n")

#문자열의 길이 : len(a)
a = "Life is too short"
print(len(a))

#문자열 인덱싱
print(a[3])

print(a[-1]) # -1은 뒤에서부터 세는 것이다.(여기선 t)

'''
문자열 슬라이싱 : 변수[시작인덱스:종료인덱스],
종료 인덱스에 해당하는 것은 출력되지 않는다.
종료 인덱스를 생략하면 문자열 끝까지 뽑아낸다
시작 인덱스를 생략하면 처음부터 종료인덱스까지 뽑아넨다
둘다 생략하면 처음부터 끝까지다.
마이너스 기호도 사용할 수 있다.
'''
print(a[0:4]) # Life
print(a[0:3]) # Lif
print(a[:4])
print(a[3:])
print(a[:])
print(a[1:-1])

#문자열 요솟값은 바꿀 수 없는 값이다.
#따라서 슬라이싱이 필수적이다.

#문자열 포매팅
# 1개 값 : % var1
d = 5
print("I ate %d apple" % d)

# 2개 이상의 값 대입 : % (var1, var2)
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# %s는 정수는 소수든 다 문자열로 바꾸기 때문에 복잡하게 생각x

# 문자열 내에서 %를 표현하려면 %%를 쓰자.


# 정렬
'''
"%10s" % 'hi' // 10개인 문자열 공간에서 오른쪽 정렬하고 나머지는 공백이다.
-10은 왼쪽 정렬이다.
"%-10sjane" % hi는 hi         jane이 된다. // 10개인 문자열 공간에서 hi는 왼쪽정렬하고 나머지는
공백으로 채운 뒤, 공간 뒤에 jane이 온다.

'''

# 책 61p까지
