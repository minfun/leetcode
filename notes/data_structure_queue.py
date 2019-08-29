class MyQueue(object):

    def __init__(self, value=None):
        self.value = value
        self.behind = None

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return 'None'


def create_queue():
    return MyQueue()


def last(queue):
    if isinstance(queue, MyQueue):
        if queue.behind is not None:
            return last(queue.behind)
        else:
            return queue


def push(queue, ele):
    if isinstance(queue, MyQueue):
        last_queue = last(queue)
        new_queue = MyQueue(ele)
        last_queue.behind = new_queue


def pop(queue):
    if queue.behind is not None:
        get_queue = queue.behind
        queue.behind = queue.behind.behind
        return get_queue
    else:
        print('empty')


def print_queue(queue):
    print(queue)
    if queue.behind is not None:
        print_queue(queue.behind)
