# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# link: https://leetcode.com/problems/diameter-of-binary-tree/
# Wechat: creategoodthing

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 1

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.longest = max(self.longest, left + right + 1)
            return max(left, right) + 1

        depth(root)
        return self.longest - 1
