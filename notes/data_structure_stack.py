class my_stack(object):

    def __init__(self, value):
        self.value = value
        self.before = None
        self.behind = None

    def __str__(self):
        return str(self.value)


def top(stack):
    if isinstance(stack, my_stack):
        if stack.behind is not None:
            return top(stack.behind)
        else:
            return stack


def push(stack, ele):
    push_ele = my_stack(ele)
    if isinstance(stack, my_stack):
        stack_top = top(stack)
        push_ele.before = stack_top
        push_ele.before.behind = push_ele
    else:
        raise Exception()


def pop(stack):
    if isinstance(stack, my_stack):
        stack_top = top(stack)
        if stack_top.before is not None:
            stack_top.before.behind = None
            stack_top.behind = None
            return stack_top
        else:
            print('top')
