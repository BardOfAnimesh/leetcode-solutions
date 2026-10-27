# ======================================
# LeetCode Problem: binary tree right side view
# Language: python
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# Synced by: LinkCode
# Date: 10/27/2026, 11:57:11 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    import collections
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        q=collections.deque([root])
        result=[]
        while q:
            level_size=len(q)
            for _ in range(level_size):
                node=q.popleft()
                if _ ==level_size-1:
                    result.append(node.val)
        
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return result
