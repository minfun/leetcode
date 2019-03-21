# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Link: https://leetcode.com/problems/two-sum/#/description
# Wechat: creategoodthing


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
