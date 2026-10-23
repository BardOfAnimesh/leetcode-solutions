# ======================================
# LeetCode Problem: lowest common ancestor of a binary search tree
# Language: python
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Synced by: LinkCode
# Date: 10/23/2026, 8:46:30 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root==p or root==q:
            return root
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root#it is for if q and p are to left or righ or vice versa of a node ultimately that node is the lac or if the node is equal to p or q we directly get root=lac