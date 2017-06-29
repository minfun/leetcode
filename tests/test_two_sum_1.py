# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/two-sum/#/description
import unittest
from two_sum_1 import Solution


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_two_sum_2(self):
        nums = [2, 1, 9, 4, 4, 56, 90, 3]
        target = 8
        self.assertEqual(self.solution.twoSum(nums, target), [3, 4])

    def test_none(self):
        nums = []
        target = 0
        self.assertEqual(self.solution.twoSum(nums, target), None)
