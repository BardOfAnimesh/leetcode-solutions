# ======================================
# LeetCode Problem: minimum moves to equal array elements
# Language: python
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Synced by: LinkCode
# Date: 11/1/2026, 6:22:36 PM
# ======================================


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)