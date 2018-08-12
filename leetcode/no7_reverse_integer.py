# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/reverse-integer/#/description


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
