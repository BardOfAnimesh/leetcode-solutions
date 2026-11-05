# ======================================
# LeetCode Problem: find the distance value between two arrays
# Language: python
# Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Synced by: LinkCode
# Date: 11/5/2026, 8:18:41 PM
# ======================================


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n=len(arr1)
        count=set()
        for i in range(n):
            for j in range(len(arr2)):
                
                if abs(arr1[i]-arr2[j])<=d:
                    count.add(i)
                    break
        finalres=len(arr1)-len(count)
        return finalres