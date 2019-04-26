class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        is_upper = []
        for i in word:
            if i == i.upper():
                is_upper.append(True)
            else:
                is_upper.append(False)

        mark = True
        for upper in is_upper:
            if upper != is_upper[0]:
                mark = False
                break

        if not mark:
            if is_upper[0] == True:
                for upper in is_upper[1:]:
                    if upper == True:
                        mark = False
                        return mark
                return True
            else:
                return False
        else:
            return mark


if __name__ == '__main__':
    a = Solution()
    print a.detectCapitalUse('Leetcode')
