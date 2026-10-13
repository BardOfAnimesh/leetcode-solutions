# ======================================
# LeetCode Problem: maximum alternating sum of squares
# Language: python
# Link: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Synced by: LinkCode
# Date: 10/13/2026, 10:46:29 PM
# ======================================


class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        for i in range(k):
            nums[i]=nums[i]**2
        
        nums.sort()
        
        final_res=sum(nums[k//2:])-sum(nums[:k//2])

        return final_res