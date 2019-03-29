# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Wechat: creategoodthing

import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print 'thread {}, @number: {}'.format(self.name, i)
            time.sleep(1)


def main():
    print 'Start main threading'
    threads = [MyThread() for i in range(3)]
    for t in threads:
        t.start()

    print 'End Main threading'


def reentrant_thread():
    mutex = threading.RLock()

    class MyThread(threading.Thread):

        def run(self):
            if mutex.acquire(1):
                print "thread {} get mutex".format(self.name)
                time.sleep(1)
                mutex.acquire()
                mutex.release()
                mutex.release()


if __name__ == '__main__':
    main()
