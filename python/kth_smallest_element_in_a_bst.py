# ======================================
# LeetCode Problem: kth smallest element in a bst
# Language: python
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Synced by: LinkCode
# Date: 11/17/2026, 12:19:50 AM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count=0
        self.ans=0
        def kthsearch(node):
            

            if not node:
                return False
            kthsearch(node.left)
            self.count+=1
            if self.count==k:
                self.ans=node.val
                return self.ans
            kthsearch(node.right)
            
            
        kthsearch(root)
        return self.ans
