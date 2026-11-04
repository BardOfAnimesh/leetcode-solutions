# ======================================
# LeetCode Problem: container with most water
# Language: python
# Link: https://leetcode.com/problems/container-with-most-water/
# Synced by: LinkCode
# Date: 11/4/2026, 7:55:12 PM
# ======================================


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        volume=0
        while left<right:
            h=min(height[left],height[right])
            width=right-left
            volume=max(volume,(width*h))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return volume