# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/task-scheduler/#/description

import collections
import unittest


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


class Test(unittest.TestCase):

    def setUp(self):
        self.task_schedule = Solution()

    def test_task_schedule(self):
        # AXAXA
        tasks = ['A', 'A', 'A']
        n = 1
        self.assertEqual(self.task_schedule.leastInterval(tasks, n), 5)

    def test_task_schedule_2(self):
        # A00A00AXX
        # ABCABCAD
        tasks = ['A', 'B', 'A', 'C', 'A', 'B', 'C', 'D']
        n = 2
        self.assertEqual(self.task_schedule.leastInterval(tasks, n), 8)

if __name__ == '__main__':
    unittest.main()
