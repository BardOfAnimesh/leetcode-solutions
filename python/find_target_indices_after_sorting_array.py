# ======================================
# LeetCode Problem: find target indices after sorting array
# Language: python3
# Link: https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Synced by: LinkCode
# Date: 10/19/2026, 6:03:13 PM
# ======================================


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_than=0
        copies_count=0
        final_res=[]

        for i in range(len(nums)):
            if nums[i]<target:
                less_than+=1
            
            elif nums[i]==target:
                copies_count+=1
        
        for j in range(copies_count):
            final_res.append(less_than+j)
        return final_res