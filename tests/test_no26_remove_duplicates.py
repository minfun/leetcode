# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description

import unittest
from leetcode.no26_remove_duplicates import Solution


class Test(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_remove_duplicates_1(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2, 3]), 3)

    def test_remove_duplicates_2(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2, 2, 2, 3, 3]), 3)

    def test_remove_duplicates_none(self):
        self.assertEqual(self.solution.removeDuplicates([]), 0)
