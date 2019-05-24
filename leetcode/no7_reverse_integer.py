# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# link: https://leetcode.com/problems/reverse-integer/#/description
# Wechat: creategoodthing


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


class Solution2:
    def reverse(self, x):
        r = x // max(1, abs(x)) * int(str(abs(x))[::-1])
        return r if r.bit_length() < 32 or r == -2**31 else 0
