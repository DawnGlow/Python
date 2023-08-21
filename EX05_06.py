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
"""