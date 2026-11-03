# ======================================
# LeetCode Problem: minimum moves to equal array elements iii
# Language: python
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Synced by: LinkCode
# Date: 11/3/2026, 6:36:15 PM
# ======================================


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val=max(nums)
        total_moves=0
        for i in nums:
            total_moves+=max_val-i
        return total_moves