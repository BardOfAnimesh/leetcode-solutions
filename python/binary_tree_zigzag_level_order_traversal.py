# ======================================
# LeetCode Problem: binary tree zigzag level order traversal
# Language: python
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Synced by: LinkCode
# Date: 10/28/2026, 6:32:57 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    import collections
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=collections.deque([root])
        result=[]
        level=0
        while q:
            level_nodes=len(q)
            res=[]

            for _ in range(level_nodes):
                node=q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level%2==0:
                result.append(res)
            else:
                result.append(res[::-1]) 
                
                    
            level+=1
        return result