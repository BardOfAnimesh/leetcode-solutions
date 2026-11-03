# ======================================
# LeetCode Problem: minimum moves to equal array elements iii
# Language: python
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# Synced by: LinkCode
# Date: 11/3/2026, 6:37:35 PM
# ======================================


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(nums)*max(nums)-sum(nums)