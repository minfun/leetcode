# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[flag]:
                flag += 1
                nums[flag] = nums[i]
        return flag + 1
