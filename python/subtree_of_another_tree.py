# ======================================
# LeetCode Problem: subtree of another tree
# Language: python
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Synced by: LinkCode
# Date: 10/25/2026, 6:31:29 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        
        def chkSubtree(node,subnode):
            if not node and not subnode:
                return True
            elif (not node and subnode)or (not subnode and node):
                return False

            if node.val != subnode.val:
                return False

            return chkSubtree(node.left, subnode.left) and chkSubtree(node.right, subnode.right)
        
        if not root:
            return False
        if root and subRoot:
            if root.val==subRoot.val:
                if chkSubtree(root,subRoot):
                    return True
        
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
