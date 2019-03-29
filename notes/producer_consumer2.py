# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Wechat: creategoodthing
import threading
import time
import Queue


q = Queue.Queue(10)


def producer(worker, q):
    count = 0
    while True:
        if not q.full():
            q.put(count)
            print '{} produce {}, qsize {}'.format(worker, count, q.qsize())
            count += 1
        time.sleep(0.3)


def consumer(name, q):
    while True:
        print '{} consume {}'.format(name, q.get())
        time.sleep(1)
        if q.qsize() == 0:
            break


def main():
    p1 = threading.Thread(target=producer, args=('lina', q))
    c1 = threading.Thread(target=consumer, args=('a', q))
    c2 = threading.Thread(target=consumer, args=('b', q))
    p1.start()
    c1.start()
    c2.start()
    p1.join()
    c1.join()
    c2.join()


if __name__ == '__main__':
    main()
