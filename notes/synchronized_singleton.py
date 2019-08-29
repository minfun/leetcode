# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Wechat: creategoodthing
import threading


def synchroinzed(func):

    lock = threading.Lock()

    def warpper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return warpper


class Singletion(object):
    instance = None

    @synchroinzed
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            print('new instance')
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self, num):
        print('num')
        print(num)
        print('add 1')
        self.a = num + 1

    def printf(self):
        print(self.a)


def _synchronized_singleton(num):
    singletion = Singletion(num)
    print('_synchronized_singleton')
    print(singletion)
    print('id')
    print(id(singletion))
    return singletion


if __name__ == '__main__':
    task_list = []
    for i in range(30):
        t = threading.Thread(target=_synchronized_singleton(i))
    for task in task_list:
        task.start()
    for task in task_list:
        task.join()
