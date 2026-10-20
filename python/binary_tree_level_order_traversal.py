# ======================================
# LeetCode Problem: binary tree level order traversal
# Language: python
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Synced by: LinkCode
# Date: 10/20/2026, 12:43:23 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        import collections
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]
        
        q=collections.deque([root])

        def bfs(node,level):
            while q:
                level_size=len(q)
                current_lvl=[]
                for i in range(level_size):
                    node=q.popleft()
                    current_lvl.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                result.append(current_lvl)
        bfs(root,0)
        return result       