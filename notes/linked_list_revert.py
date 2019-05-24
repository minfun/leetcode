#!/usr/bin/python
# 递归实现单链表反转


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
    print('head.val')
    print(head.val)
    if head is None:
        print('head is none')
        return
    if head.next is None:
        print('head next is none')
        newhead = head
    else:
        print('recurse')
        newhead = recurse(head.next, newhead)
        print('recurse head')
        print(head.val)
        print('newhead.val')
        print(newhead.val)
        head.next.next = head
        head.next = None
    return newhead


if __name__ == '__main__':
    head = ListNode(1)  # 测试代码
    p1 = ListNode(2)  # 建立链表1->2->3->4->None
    p2 = ListNode(3)
    p3 = ListNode(4)
    head.next = p1
    p1.next = p2
    p2.next = p3
    newhead = None
    p = recurse(head, newhead)  # 输出链表4->3->2->1->None
    while p:
        print(p.val)
        p = p.next
