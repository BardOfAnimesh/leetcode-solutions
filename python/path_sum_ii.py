# ======================================
# LeetCode Problem: path sum ii
# Language: python
# Link: https://leetcode.com/problems/path-sum-ii/
# Synced by: LinkCode
# Date: 10/8/2026, 10:17:08 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        
        """
        if not root:
            return []
        result = []
        lst1 = [root.val]
        remaining_sum = targetSum - root.val

        def recursive_path(node, remaining_sum, result, lst1):
            

            if not node.left and not node.right:
                if remaining_sum == 0:
                    ans=lst1[:]
                    result.append(ans)
                    return 

            if node.left:
                lst1.append(node.left.val)
                recursive_path(node.left, remaining_sum-node.left.val, result, lst1)
                lst1.pop()
            if node.right:
                lst1.append(node.right.val)
                recursive_path(node.right, remaining_sum-node.right.val, result, lst1)
                lst1.pop()                    
                
        recursive_path(root, remaining_sum, result, lst1)
        return result