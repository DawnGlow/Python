# 문자열

"""
*** 문자열을 만드는 방법 ***
1. 큰따옴표로 둘러싸기
"ㅁㅁㅁ"
2. 작은 따음표로 둘러싸기
'ㅁㅁㅁ'
3. 큰따음표 3개를 연속으로 써서 둘러싸기
4. 작은따옴표 3개를 연속으로 써서 둘러싸기

그럼 이것을 쓰는 기준은 뭘까?

* 문자열에 작은따옴표(')가 있는 경우
큰따옴표로 둘러싸자. (작은 따옴표 사용 시 syntax error 발생)

* 문자열에 큰따옴표(")가 있는 경우
작은 따옴표로 둘러싸자. 

* 다른방법
백슬래쉬 + 따옴표 조합 ex)
food = 'python \'s favorite food is perl'
say = "\"Python is very easy.\" he says."


*** 여러줄의 문자열 대입 ***
* multiline = "abc\ndef" --> 불편함

* 연속으로 작은따옴표 3개 또는 큰 따옴표 3개 사용하기
multiline = '''
Life is too short
You need python
'''

*** 이스케이프 코드 ***
\n : 줄바꿈
\t : 탭간격
\\ : \표현
\r : 캐리지 리턴(줄바꿈 문자, 커서 가장앞으로)
\f : 폼피드(줄바꿈 문자, 커서 다음 줄로)
\a : 벨소리
\b : 백스페이스
\000 : 널문자

*** 문자열 연산 ***
* 더하기
head = "python"
tail = " is no jam"
head + tail
res : python is no jam

* 곱하기
head * 2
res : pythonpython
"""

print("=" * 50)
print("My Program")
print("=" * 50)

"""
*** 문자열 길이 구하기 ***
a = "Life is too short"
len(a)
result : 17

*** 문자열 인덱싱 ***
a = "Life is too short"
여기서
a[3]
res : 'e'
L부터 0번인덱스이다.

a[-1]
res : 't'
-1은 뒤에서부터 첫번째라는 의미이다. 

헷갈리지 말자. a[1]은 앞에서 두번째이지만, a[-1]은 뒤에서 첫번째이다.

a[0] == a[-0] 이다

*** 문자열 인덱싱 ***
* 문자열에서 일부 문자열을 뽑아내기
a = "Life is too short"
a[0:4] 
res : Life
a[0:3]
res : Lif

--> 인덱싱 끝 번호는 포함하지 않는다. 0:3은 0,1,2만 포함

a[10:]
--> 시작번호부터 끝까지

a[:17]
--> 처음부터 16까지 출력

a[:]
--> 처음부터 끝까지

a = "Life is too short, You need Python"

a[19:-7]
res : 'You need'

*** 문자열의 요솟값은 바꿀 수 없다 ***
a = "pithon"
a[1] = 'y' 이런건 안된다.


*** 문자열 포매팅 ***
: 문자열 안에 어떤 값을 삽입하는 방법
1. 숫자 바로 대입
"I eat %d apples." % 3
res : 'I eat 3 apples.'

2. 문자열 바로 대입
"I eat %s apples." % "five"

3. 변수 대입
number = 5
"I eat %d apples." % number

4. 2개 이상의 값을 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days" % (number, day)

* 문자열 포맷 코드
c랑 똑같음

번외) %s 포맷 코드
3을 %s로 받으면 문자열 3으로 받는다.

* 문자열 안에 퍼센트 넣기
"Error is %d%%." % 98


*** 포맷 코드의 숫자사용 ***
1. 정렬과 공백
"%10s" % "hi"
res: '        hi'
---> 전체 길이가 10인 문자열에서 오른쪽 정렬하고 나머지는 공백으로
"%-10s" % "hi"
---> 전체 길이가 10인 문자열에서 왼쪽 정렬하고 나머지는 공백으로

2. 소수점 표현
"%0.4f" % 3.42134234
res : 3.4213
--> 4개의 소숫점만 출력해라라는 의미이다.

"%0.4f" % 3.42134234
res : '    3.4213'
--> w전체 길이가 10인 문자열에서 오른쪽 정렬하고, 나머지 공백처리, 소숫점은 4개까지 표시.


*** format 함수를 사용한 포매팅 ***

1. 숫자 바로대입
"I eat {0} apples".format(3)
2. 문자열 바로 대입
"I eat {0} apples".format("five")
3. 숫자 변수 대입
number = 3
"I eat {0} apples".format(number)
4. 두개 이상의 값 넣기
number = 10
day = three
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
--> {0}, {1}과 같은 인덱스 항목이 format 함수의 입력 값으로 바뀜.
5. 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
6. 인덱스 + 이름 혼용
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
"""