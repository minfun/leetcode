# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/two-sum/#/description

import unittest


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = target - nums[i]
            nums[i] = 'X'
            if temp in nums:
                return [i, nums.index(temp)]
        return None


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

if __name__ == '__main__':
    unittest.main()
