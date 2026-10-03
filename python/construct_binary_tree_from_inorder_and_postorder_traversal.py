# ======================================
# LeetCode Problem: construct binary tree from inorder and postorder traversal
# Language: python
# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Synced by: LinkCode
# Date: 10/3/2026, 6:28:56 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None

        val=postorder.pop()
        index=inorder.index(val)
        root=TreeNode(val)


        root.right=self.buildTree(inorder[index+1:],postorder)
        root.left=self.buildTree(inorder[:index],postorder)
        

        return root
