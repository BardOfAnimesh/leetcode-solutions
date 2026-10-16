# ======================================
# LeetCode Problem: diameter of binary tree
# Language: python
# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# Synced by: LinkCode
# Date: 10/17/2026, 12:16:13 AM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_dia=0

        def node_search(node):
            if not node:
                return 0
            
            left=node_search(node.left)
            right=node_search(node.right)
            self.max_dia=max(self.max_dia,left+right)

            return 1+max(left,right)
        node_search(root)

        return self.max_dia