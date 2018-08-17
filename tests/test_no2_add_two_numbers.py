# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Link: https://leetcode.com/problems/add-two-numbers/#/description
import unittest
from leetcode.no2_add_two_numvers import Solution
from leetcode.no2_add_two_numvers import LinkedList


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
