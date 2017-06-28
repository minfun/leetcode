# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/reverse-integer/#/description

import unittest


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pre = cmp(x, 0)
        reverse = int(str(abs(x))[::-1])
        if reverse >= 2**31:
            return 0
        return pre*reverse

    def reverse_method2(self, x):
        s = cmp(x, 0)
        r = int(`s * x`[::-1])
        return s * r * (r < 2 ** 31)


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

if __name__ == '__main__':
    unittest.main()
