# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/task-scheduler/#/description

import collections


class Solution:

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count = collections.Counter(tasks).values()
        print task_count
        M = max(task_count)
        print M
        M_M = task_count.count(M)
        print M_M
        print (M - 1)*(n + 1) + M_M
        return max(len(tasks), (M - 1)*(n + 1) + M_M)
