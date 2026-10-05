# ======================================
# LeetCode Problem: path sum
# Language: python
# Link: https://leetcode.com/problems/path-sum/
# Synced by: LinkCode
# Date: 10/5/2026, 10:42:31 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        remaining_sum=targetSum-root.val
        if (not root.right and not root.left) and remaining_sum==0:
            return True

        return self.hasPathSum(root.right,remaining_sum) or self.hasPathSum(root.left,remaining_sum)