# ======================================
# LeetCode Problem: balanced binary tree
# Language: python
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Synced by: LinkCode
# Date: 10/22/2026, 8:42:31 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.final_res=True

        def balancecheck(node):
            if not node:
                return 0

            
            left=balancecheck(node.left)
            right=balancecheck(node.right)
            
            if abs(left-right)>1:
                self.final_res =False
            if not self.final_res:
                return self.final_res
            return max(left,right)+1
        balancecheck(root)
        return self.final_res