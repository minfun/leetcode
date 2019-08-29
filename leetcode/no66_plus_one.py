class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_str = int(''.join(map(lambda x: str(x), digits))) + 1
        return list(map(lambda x: int(x), list(str(digit_str))))

    def plusOne2(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits
