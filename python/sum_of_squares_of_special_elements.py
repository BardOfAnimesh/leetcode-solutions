# ======================================
# LeetCode Problem: sum of squares of special elements
# Language: python
# Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Synced by: LinkCode
# Date: 10/12/2026, 12:43:41 AM
# ======================================


class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        total=0
        for i in range(length):
            if length%(i+1)==0:
                total+=(nums[i])**2

        return total