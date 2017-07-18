# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            print 'for'
            print i
            print ch
            print dic
            if ch in dic:
                print 'in'
                print res, i-start
                # update the res
                res = max(res, i-start)
                print 'res'
                print res
                print start, dic[ch] + 1
                # here should be careful, like "abba"
                start = max(start, dic[ch]+1)
                print 'start'
                print start
            dic[ch] = i
            print 'end'
        # return should consider the last
        # non-repeated substring
        print 'out'
        print res, len(s) - start
        return max(res, len(s)-start)

if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring('asdfaebd')