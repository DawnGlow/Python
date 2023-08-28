# EX06_06 하위 디렉토리 검색
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass


search("/usr/bin")

# os.walk 사용 --> 시작디렉토리부터 하위 모든 디렉토리를 차례대로 방문
for (path, dir, files) in os.walk("/Users/luna/Desktop"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print(f'{path}, {filename}')
