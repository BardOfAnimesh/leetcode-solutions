# ======================================
# LeetCode Problem: 3sum
# Language: python
# Link: https://leetcode.com/problems/3sum/
# Synced by: LinkCode
# Date: 9/30/2026, 9:34:24 PM
# ======================================


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        for i in range (len(nums)):
            l=i+1
            r=len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r :
                total=nums[i]+nums[l]+nums[r]
                if total==0 :
                    result.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1 
                    while l<r and nums[r]==nums[r+1]:
                        r-=1           
                elif total<0:
                    l+=1
                elif total>0:
                    r-=1
        return result