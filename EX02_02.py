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

"%10.4f" % 3.42134234
res : '    3.4213'
--> w전체 길이가 10인 문자열에서 오른쪽 정렬하고, 나머지 공백처리, 소숫점은 4개까지 표시.


*** format 함수를 사용한 포매팅 ***

1. 숫자 바로대입
"I eat {0} apples".format(3)
"My name is {} and my room is {}".format('choi', 327)
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
7. 왼쪽 정렬
"{0:<10}".format("hi")
-->   :<10  표현식은 치환되는 문자열을 왼쪽으로 정렬, 문자열의 자릿수를 10으로 맞춘다.
8. 오른쪽 정렬
"{0:>10}".format("hi")
-->   :>0  표현식은 치환되는 문자열을 오른쪽으로 정렬, 문자열의 자릿수를 10으로 맞춘다.
9. 가운데정렬
"{0:^10}".format("hi")
-->   :^기홀를 사용한다.
10. 공백채우기
"{0:=^10}".format("hi")
---> :와 {<, >, ^} 사이에 공백을 채울 문자를 넣으면 공백 문자 대신에 해당 문자로 채워넣는다.
"{0:!<10}".format("hi")
11. 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
--> {0}에서 0 뒤에 :0.4f를 사용하여 소수점 4자리만 표현
"{0:10.4f}".format(y)
--> 자릿수를 10으로 맞추고 오른쪽 정렬, 소수점 4자리만 표현
12. { 또는 } 문자 표현하기
"{{ and }}".format()
--> 중괄호 문자 그대로 사용하고 싶으면 중괄호를 두번 연속 사용하면 된다.

*** f 문자열 포매팅 (python 3.6부터) ***

* Base : 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 사용 가능.
name = '홍길동'
age = 30
f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.'

* 표현식도 사용 가능하다. (변수끼리의 수식)
f'나는 내년이면 {age + 1}살이 된다.'

* 딕셔너리도 사용 가능하다.
d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]} 입니다. 나이는 {d["age"]} 입니다.'

* f 포매팅 정렬
f'{"hi":<10}'
f'{"hi":>10}'
f'{"hi":^10}'

* f 포매팅 공백 채우기
f'{"hi":=^10}'
f'{"hi":!<10}'

* f 포매팅 소수 표현
y = 3.42134234
f'{y:0.4f}'
f'{y:10.4f}'

* f 포매팅 중괄호 표현
f'{{ and }}'

* Q1. answer 1 (format 함수)
"{0:!^12}".format("python")

* Q2. answer 2 (f 포매팅)
f'{"python":!^12}'


*** 문자열 관련 함수 ***

* 문자 개수 세기 (count 함수)
a = "hobby"
a.count('b')
res : 2
--> 문자열중 매개변수 안에 있는 문자의 갯수를 return

* 위치 알려주기1(find 함수)
a = "python is the best choice"
a.find('b')
res : 14
---> 문자열 b가 처음 나온 위치를 리턴한다.
a.find('k')
res : -1
---> 문자열에 없으면 -1을 반환한다.

* 위치 알려주기2(index 함수)
a = "Life is too short"
a.index('t')
res : 8
---> 문자 t가 처음나온 위치를 반환
find와 차이점이라면 없는 문자를 찾으려하면 오류를 발생시킨다.

* endswith 함수
line.endswith('.') --> line이 {argument}로 끝나면 True / 아니면 False 반환

* startswith 함수
line.startswith('.')--> line이 {argument}로 시작하면 True/ 아니면 False

* 문자열 삽입(join 함수)
",".join('abcd')
res : 'a,b,c,d'
---> abcd 문자열의 각각 문자 사이에 ,를 삽입한다.

ex) 리스트에서 사용
",".join(['a', 'b', 'c', 'd'])
res : 'a,b,c,d'

* 소문자를 대문자로 바꾸기(upper 함수)
a = "hi"
a.upper()
res : 'HI'

* 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()
res : hi

* 왼쪽 공백 지우기(lstrip 함수)
a = " hi "
a.lstrip()
res : 'hi '

* 오른쪽 공백 지우기(rstrip 함수)
a = " hi "
a.rstrip()
res : ' hi'

* 양쪽 공백 지우기(strip)
a = " hi "
a.strip()
res : 'hi'

* strip(parameter)
ex)
full_name = '\t junseo Bae \n'
full_name.strip() # 'junseo Bae'
full_name.strip('\t\n') # ' junseo Bae '
full_name.lstrip() # 'junseo Bae \n'
full_name.rstrip() # '\t junseo Bae'

* 문자열 바꾸기 (replace 함수)
a = "Life is too short"
a.replace("Life", "Your leg")
res : 'Your leg is too short'
--> replace(바뀌게 될 문자열, 바꿀 문자열)

* 문자열 나누기(split 함수)
a = "Life is too short"
a.split() // 공백을 기준으로 문자열 나눔
res : ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':') // :를 기준으로 문자열 나눔
res : ['a', 'b', 'c', 'd']

* 문자열 \n을 기준으로 나누기(splitlines 함수)
profs = 'choi, 327, 1\nKang, 328, 1'
profs.splitlines() # ['choi, 327, 1', 'Kang, 328 ,1']
"""