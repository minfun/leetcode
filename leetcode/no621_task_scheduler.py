# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Link: https://leetcode.com/problems/task-scheduler/#/description
# Wechat: creategoodthing
import collections


class Solution:

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = collections.Counter(tasks).values()
        M = max(task_count)
        M_M = task_count.count(M)
        return max(len(tasks), (M - 1)*(n + 1) + M_M)
