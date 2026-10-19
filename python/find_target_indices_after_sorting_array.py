# ======================================
# LeetCode Problem: find target indices after sorting array
# Language: python
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Synced by: LinkCode
# Date: 10/19/2026, 5:51:47 PM
# ======================================


class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        final_res=[]

        for i in range(len(nums)):
            if nums[i]==target:
                final_res.append(i)
        

        return final_res