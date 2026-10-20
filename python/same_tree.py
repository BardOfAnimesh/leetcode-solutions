# ======================================
# LeetCode Problem: same tree
# Language: python
# Link: https://leetcode.com/problems/same-tree/
# Synced by: LinkCode
# Date: 10/21/2026, 1:03:34 AM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        res=True
        if not p and not q:
            res=True
            return res
        if not p or not q or p.val != q.val:
            return False
            
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
    