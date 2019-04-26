class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        times = 0
        for i in range(len(s)):
            if s[i] == 'A':
                times += 1
            if times == 2:
                return False
            if i <= len(s)-3:
                if s[i] == 'L' and s[i+1] == 'L' and s[i+2] =='L':
                    return False
        return True


if __name__ == '__main__':
    a = Solution()
    print a.checkRecord('AA')
