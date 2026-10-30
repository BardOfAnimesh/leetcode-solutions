# ======================================
# LeetCode Problem: flatten binary tree to linked list
# Language: python
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Synced by: LinkCode
# Date: 10/31/2026, 1:38:47 AM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def preorder(node):
            if not node:
                return
            left=preorder(node.left)
            right=preorder(node.right)
            
            if left:
                temp=node.right
                left.right=temp
                node.right=node.left
                node.left=None
            return right or left or node
        preorder(root)
        