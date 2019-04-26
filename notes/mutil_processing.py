from multiprocessing import Process
import time
import os


def f(name):
    time.sleep(2)
    print("hello", name)


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print('\n\n')


def f2(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    # p = Process(target=f, args=('bob',))
    # p.start()
    # p.join()

    info('\033[32;1mmain process line\033[0m')
    p2 = Process(target=f2, args=('bob',))
    p2.start()
    p2.join()


