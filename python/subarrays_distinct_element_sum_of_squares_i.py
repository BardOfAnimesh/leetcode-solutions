# ======================================
# LeetCode Problem: subarrays distinct element sum of squares i
# Language: python
# Link: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Synced by: LinkCode
# Date: 10/16/2026, 12:34:22 AM
# ======================================


class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                total_sum+=len(seen)**2

        return total_sum