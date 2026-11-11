# ======================================
# LeetCode Problem: binary tree maximum path sum
# Language: python
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Synced by: LinkCode
# Date: 11/11/2026, 10:09:04 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxval=float('-inf')
        def max_gain(node):
            if not node:
                return 0
            left=max(0,max_gain(node.left))
            right=max(0,max_gain(node.right))

            curr_max_path=node.val+left+right
            self.maxval = max(self.maxval, curr_max_path)
            
            return node.val+max(left,right)

        max_gain(root)
        return self.maxval
