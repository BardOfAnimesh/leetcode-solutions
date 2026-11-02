# ======================================
# LeetCode Problem: minimum moves to equal array elements ii
# Language: python
# Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Synced by: LinkCode
# Date: 11/2/2026, 10:04:42 PM
# ======================================


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median=nums[len(nums)//2]
        finalmoves=0
        for i in nums:
            finalmoves+=abs(i-median)
        return finalmoves

