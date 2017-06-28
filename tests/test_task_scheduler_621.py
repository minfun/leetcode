# Github: https://github.com/minfun/leetcode
# Email: minfun@live.com
# link: https://leetcode.com/problems/task-scheduler/#/description
import unittest
from task_scheduler_621 import Solution


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
