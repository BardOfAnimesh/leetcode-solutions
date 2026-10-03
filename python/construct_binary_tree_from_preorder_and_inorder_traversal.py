# ======================================
# LeetCode Problem: construct binary tree from preorder and inorder traversal
# Language: python
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Synced by: LinkCode
# Date: 10/3/2026, 6:57:45 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        val=preorder.pop(0)
        root= TreeNode(val)
        index=inorder.index(val)

        root.left=self.buildTree(preorder,inorder[:index])
        root.right=self.buildTree(preorder,inorder[index+1:])

        return root