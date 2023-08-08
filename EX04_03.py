# 파일 읽고 쓰기

"""
# 파일 생성하기
ex)
"""

f = open("new_file.txt", 'w') # 파이썬 내장함수 open(파일이름, 파일 열기 모드)
f.close()

"""
* 파일 열기 모드
r : 읽기 모드 - 파일을 읽기만 할 때 사용
w : 쓰기 모드 - 파일에 내용을 쓸 때 사용 # 해당 파일이 이미 존재하는 경우 내용이 모두 사라지고, 파일이 없으면 새로 생성됨.
    특정 경로에 생성하고 싶으면 디렉토리까지 적어주자.
a : 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용

f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 함. 생략해도 자동으로 닫아주긴 하지만,
쓰기 모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생함.

# 파일을 쓰기 모드로 열어서 출력값 적기
ex)
"""
f = open("new_file.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

"""
print(data) 와 f.write(data)는 출력하는 방법이 다르다.
print는 프롬프트(터미널, 콘솔)에, f.write는 파일에 결괏값을 출력한다


# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법

* readline 함수 사용하기
ex) 첫번째 줄만 출력
"""
f = open("new_file.txt", 'r')
line = f.readline()
print(line)
f.close()

"""
- 모든 줄을 읽어서 출력
ex)
"""
f = open("new_file.txt", 'r')
while True:
    line = f.readline() # 더 이상 읽을 줄이 없으면 None을 출력한다.
    if not line: break
    print(line)
f.close()

"""
* readlines 함수 사용하기
ex)
"""

f = open("new_file.txt", 'r')
lines = f.readlines() # readlines 함수는 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려줌.
for line in lines:
    print(line)
f.close()

"""
* read 함수 사용하기
ex)
"""
f = open("new_file.txt", 'r')
data = f.read() # f.read()는 파일의 내용 전체를 문자열로 돌려준다.
print(data)
f.close()

"""

# 파일에 새로운 내용 추가하기
- 기존에 있는 내용을 살리고 새로운 값만 추가하고 싶음
- 추가모드 'a'로 열면 됨.
ex)
"""

f = open("new_file.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

"""

# with문과 함께 사용하기

- with문을 사용하여 파일을 열고 닫는 걸 자동으로 처리
ex)
"""

with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")

# with 블록을 벋어나는 순간 f가 자동으로 close됨.

"""
# sys 모듈로 매개변수 주기

명령 프롬프트 명령어 [인수1 인수2 ...]

ex)
import sys
args = sys.argv[1:]
for i in args:
    print(i)

sys 모듈의 argv는 명령창에서 입력한 인수를 의미.
argv[0]는 파일 이름 sys1.py가 되고, argv[1]부터 나오는 인수가 argv의 요소가 된다.
"""