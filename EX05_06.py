# 라이브러리(Library)

"""
# sys 모듈
- 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

* sys.argv
- 명령행에서 인수 전달하기
ex) python test.py abc pey guido
--> 파일이름 뒤에 있는 값들이 sys.argv 리스트에 추가됨

* sys.exit()
- 강제로 스크립트 종료하기
- ctrl z 나 ctrl d 와 같은 기능

* sys.path
- 자신이 만든 모듈 불러와 사용하기
- sys.path는 파이썬 모듈들이 저장되어 있는 위치를 나타냄. 이 위치에 있는 모듈은 경로에 상관없이 어디에서나 불러올 수 있음.
ex)
# path_append.py
import sys
sys.path.append("C:/doit/Mymod")
--> 경로 이름을 추가해 해당 경로에 있는 모듈을 불러올 수 있음


# pickle
- 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
ex) pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체 data를 그대로 저장하는 방법
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'You need'}
pickle.dump(data, f)
f.close()
ex) pickle.dump로 저장한 파일을 pickle.load를 이용해 원래 있던 딕셔너리 객체 상태 그대로 불러오는 예
import pickle
f = open("test.txt", 'rb')
data = picle.load(f)
print(data)
res : {1: 'python', 2: 'You need'}

# OS
- 환경 변수나 디렉토리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈

* os.environ
- 내 시스템의 환경변수 값을 알고 싶을 때 사용
ex)
>>> import os
>>> os.environ
environ({딕셔너리 객체}) # ('PROGRAMFILES': 'C:\\Program Files', ....) 이런식으로 나옴
>>>

- 돌려받은 객체가 딕셔너리 객체기 때문에, 호출해서 원하는 값을 얻을 수도 있음
ex) os.environ['PATH'] # res : 'C:\\ProgramData\\Oracle\\Java\\javapath; ... 생략 ...'

* os.chdir
- 디렉토리 위치 변경하기
ex) os.chdir("C:\WINDOWS")

* os.getcwd
- 디렉토리 위치 돌려받기
ex) os.getcwd() # res : 'C:\WINDOWS'

* os.system
- 시스템 명령어 호출하기
- 시스텀 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수 있음
ex) 현재 디렉토리에서 시스템 명령어 ls을 실행하는 예
>>> os.system("ls")

* os.popen
- 실행한 시스템 명령어의 결괏값을 읽기 모드 형태의 파일 객체로 돌려줌
ex) f = os.popen("ls")
print(f.read())

* 기타 유용한 os 관련 함수
- os.mkdir(디렉토리) : 디렉토리 생성
- os.rmdir(디렉토리) : 디렉토리 삭제(비어있어야 가능)
- os.unlink(파일 이름) : 파일을 지운다
- os.rename(src, dst) : src라는 이름의 파일을 dst라는 이름으로 바꾼다.

# shutil

- 파일을 복사해주는 파이썬 모듈
ex) src.txt 파일을 dst.txt로 복사
import shutil
shutil.copy("src.txt", "dst.txt")
- dst가 디렉토리 이름이면 src.txt 그대로 dst 디렉토리에 복사됨
- 동일한 이름이 있다면 덮어쓴다.

# glob
- 특정 디렉토리에 있는 파일 이름을 모두 알아야 할 때 주로 사용하는 모듈

* glob(pathname)
- 디렉토리에 있는 파일들을 리스트로 만들기
ex) C:/doit 디렉토리에 있는 파일 중 이름이 mark로 시작하는 파일들을 모두 찾아서 읽어들이는 예
import glob
glob.glob("C:/doit/mark*")

# tempfile
- 파일을 임시로 만들어서 사용할 때 유용한 모듈

* tempfile.mkstemp()
- 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
ex)
import tempfile
filename = tempfile.mkstemp()
filename # res : 'C:\WINDOWS\TEMP\~-275151-0'

* tempfile.TemporaryFile()
- 임시 저장 공간으로 사용할 파일 객체를 돌려줌
- 기본적으로 wb모드를 가짐
- f.close()가 호출되면 자동으로 사라짐
ex)
import tempfile
f = tempfile.TemporaryFile()
f.close() # 생성한 임시파일 자동으로 삭제

# time
- 시간과 관련된 모듈

* time.time()
- UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수
ex)
import time
time.time() # res : 1692774508.134141

* time.localtime
- time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초... 의 형태로 바꿔주는 함수
ex)
time.localtime(time.time())

* time.asctime
- time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
ex)
time.asctime(time.localtime(time.time()))
# res: 'Wed Aug 23 16:10:47 2023'

* time.ctime
- time.asctime(time.localtime(time.time()))를 time.ctime을 이용해서 간편하게 표시.
- asctime과 다른점은 ctime은 항상 현재 시간만 돌려줌
ex) time.ctime() # res : 'Wed Aug 23 16:10:47 2023'

* time.strftime
- 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷 코드 제공
- time.strftime('출력할 형식 포맷코드', time.localtime(time.time()))
- 포맷코드는 책 254P 참조
ex) import time
time.strftime('%x', time.localtime(time.time()))
# res : '08/23/23'

* time.sleep
- 루프 안에서 주로 사용
- 일정한 시간 간격을 두고 루프를 실행할 수 있다.
ex) # sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(1)

# calendar
- 파이썬에서 달력을 볼 수 있게 해주는 모듈

* calendar.calendar(연도)
- 그해의 전체 달력을 볼 수 있음

* calendar.prcal(연도)
- calendar.calendar(연도)와 같은 결괏값

* calendar.prmonth(연도, 월)
- 해당 연도의 해당 월에 해당하는 달력을 보여줌

* calendar.weekday(연도, 월, 일)
- 그 날짜에 해당하는 요일 정보를 돌려줌
- 월요일은 0, 화요일은 1, .......

* calendar.monthrange(연도, 월)
- 입력받은 달의 1일이 무슨 요일인지, 그 달이 며칠까지 있는 지를 튜플 형태로 돌려줌
ex) calendar.monthrange(2023, 8)

# random
- 난수를 발생시키는 모듈

* random.random()
- 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려줌

* random.randint(a, b)
- a에서 b 사이의 정수 중에서 난수 값을 돌려줌(a, b 포함)

ex) 입력받은 리스트의 요소중에서 무작위로 하나를 선택해 돌려줌
# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)- 1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

* random.choice(iterable)
- 입력받은 변수에서 무작위로 하나를 선택하여 돌려줌

* random.shuffle(list)
- 입력받은 리스트의 항목을 무작위로 섞어줌.

# webbrowser
- 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈

* webbrowser.open(url)
- 기본 웹브라우저를 자동으로 실행하고 해당 url로 가게 해줌
- 이미 웹브라우저가 실행된 상태라면 해당 url로 이동
- 실행되지 않은 상태라면 브라우저 실행 후 해당 url로 이동

* webbrowser.open_new(url)
- 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열림

# threading
- 컴퓨터에서 동작하고 있는 프로그램을 Process라고 함
- 보통은 1개 프로세스는 한가지 일만 하지만, 스레드를 사용하여 하나의 프로세스 안에서 2가지 이상의 일을 동시에 수행할 수 있음
ex) # thread_test.py
import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f'working: {i}\n')

print("Start")

for i in range(5):
    long_task()

print("End")

- 위 코드는 5초씩 5번 반복해 25초가 소요됨
- 스레드를 사용하여 5초에 다 끝내보자

ex) # thread_test.py
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f'working: {i}\n')
print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target = long_task) # 스레드 생성
    threads.append(t)

for t in threads:
    t.start()

print("End")

"""