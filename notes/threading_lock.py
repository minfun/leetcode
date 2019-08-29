import threading
import time


def run(n):
    global num
    num += 1


lock = threading.Lock()


def run_mutex(n):
    lock.acquire()
    global num_mutex
    num_mutex += 1
    lock.release()


num = 0
num_mutex = 0
t_obj = []
t_obj_mutex = []

for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t_m = threading.Thread(target=run_mutex, args=("t-%s" % i,))
    t.start()
    t_m.start()
    t_obj.append(t)
    t_obj_mutex.append(t_m)

for t in t_obj:
    t.join()

for t_m in t_obj_mutex:
    t_m.join()

print("num:", num)
print("num_mutex:", num_mutex)
