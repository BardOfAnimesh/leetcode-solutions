# ======================================
# LeetCode Problem: validate binary search tree
# Language: python
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Synced by: LinkCode
# Date: 10/23/2026, 2:18:31 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.final_res=True
        def validchk(node,low,high):
            if not node:
                return self.final_res
            if node.val <= low or node.val >= high:
                return False

            left= validchk(node.left,low,node.val)
            right=validchk(node.right,node.val,high)
            return left and right

        return validchk(root,-float('inf'),float('inf'))