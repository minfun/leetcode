# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/reverse-integer/#/description
import unittest
from reverse_integer_7 import Solution


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_positive_integer(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_negtive_integer(self):
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_big_positive_integer(self):
        self.assertEqual(self.solution.reverse(1534236469), 0)

    def test_big_negtive_integer(self):
        self.assertEqual(self.solution.reverse(-2147483648), 0)

    def test_normal_number(self):
        self.assertEqual(self.solution.reverse(0), 0)
        self.assertEqual(self.solution.reverse(1), 1)
        self.assertEqual(self.solution.reverse(-1), -1)

    def test_reverse_method2(self):
        self.assertEqual(self.solution.reverse_method2(-123), -321)
        self.assertEqual(self.solution.reverse_method2(123), 321)
