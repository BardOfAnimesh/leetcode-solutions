# ======================================
# LeetCode Problem: invert binary tree
# Language: python
# Link: https://leetcode.com/problems/invert-binary-tree/
# Synced by: LinkCode
# Date: 10/6/2026, 9:07:44 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        temp=root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(temp) 

        return root