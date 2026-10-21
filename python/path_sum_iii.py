# ======================================
# LeetCode Problem: path sum iii
# Language: python
# Link: https://leetcode.com/problems/path-sum-iii/
# Synced by: LinkCode
# Date: 10/21/2026, 6:27:25 PM
# ======================================


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix_map={0:1}
        def dfs(node,current_sum):
            if not node:
                return 0
            current_sum+=node.val

            valid_paths=prefix_map.get(current_sum-targetSum,0)
            prefix_map[current_sum]=prefix_map.get(current_sum,0)+1

            final_res=(valid_paths+dfs(node.left,current_sum)+dfs(node.right,current_sum))

            prefix_map[current_sum] -= 1
            return final_res
        
        return dfs(root,0)

