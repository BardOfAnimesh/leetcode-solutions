# ======================================
# LeetCode Problem: apply operations on array to maximize sum of squares
# Language: python
# Link: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
# Synced by: LinkCode
# Date: 10/13/2026, 10:24:14 PM
# ======================================


class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        final_res=0

        counts = [0] * 32
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    counts[i] += 1
        
        for _ in range(k):
            num_build=0
            for j in range(32):
                if counts[j]>0:
                    num_build+=1<<j
                    counts[j]-=1
            final_res+=num_build**2

        return final_res%MOD
            
