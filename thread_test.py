# thread_test.py
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

for t in threads:
    t.join() # join으로 스레드가 종료될 때 까지 기다림.

print("End")