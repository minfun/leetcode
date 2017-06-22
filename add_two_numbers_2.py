# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/add-two-numbers/#/description

# Definition for singly-linked list.
import unittest


class ListNode(object):

    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.node = None

    def add_node(self, data):
        new_node = ListNode(data)
        new_node.next = self.node
        self.node = new_node

    def link_as_list(self):
        data = list()
        node = self.node
        while node:
            data.append(node.val)
            node = node.next
        return data


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: LinkedList
        :type l2: LinkedList
        :rtype: LinkedList
        """
        root = n = LinkedList()
        node1 = l1.node
        node2 = l2.node
        over = 0
        while node1 or node2 or over:
            v1 = v2 = 0
            if node1:
                v1 = node1.val
                node1 = node1.next
            if node2:
                v2 = node2.val
                node2 = node2.next
            over, val = divmod(v1 + v2 + over, 10)
            n.add_node(val)
        return root


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_add_two_numbers(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l3 = LinkedList()
        l1.add_node(2)
        l1.add_node(4)
        l1.add_node(3)
        l2.add_node(5)
        l2.add_node(6)
        l2.add_node(4)
        l3.add_node(7)
        l3.add_node(0)
        l3.add_node(8)
        added = self.solution.addTwoNumbers(l1, l2).link_as_list()
        self.assertEqual(added, l3.link_as_list())


if __name__ == '__main__':
    unittest.main()
