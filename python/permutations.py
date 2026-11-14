# ======================================
# LeetCode Problem: permutations
# Language: python
# Link: https://leetcode.com/problems/permutations/
# Synced by: LinkCode
# Date: 11/15/2026, 2:13:38 AM
# ======================================


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final_res=[]
        path=[]
        def recurr_ans(nums):
            
            if len(nums)==len(path):
                return final_res.append(path[:])
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                recurr_ans(nums)
                path.pop()
        recurr_ans(nums)
        return final_res

