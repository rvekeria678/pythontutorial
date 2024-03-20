import time
import tracemalloc

tracemalloc.start()

def timer1():
    count = 0
    while True:
        count += 1
        print(count)
        time.sleep(1)

timer1()

tracemalloc.stop()