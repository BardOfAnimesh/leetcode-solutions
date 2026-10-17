# ======================================
# LeetCode Problem: minimum swaps to sort by digit sum
# Language: python
# Link: https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
# Synced by: LinkCode
# Date: 10/18/2026, 1:19:28 AM
# ======================================


class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_tab=[]
        count=len(nums)

        for i in range(count):
            remainder=0
            y=nums[i]%10
            x=(nums[i]//10)
            
            while x!=0:
                
                remainder+=y
                y=x%10
                x=(x//10)
            remainder+=y
            hash_tab.append((remainder,nums[i],i))
        hash_tab.sort()
        swap=0
        visited=[False]*count
        for j in range(count):
            if visited[j]:
                continue
            current=j
            cycle_len=0
            while not visited[current]:
                visited[current]=True
                current=hash_tab[current][2]
                cycle_len+=1
            
            if cycle_len>1:
                swap+=cycle_len-1
        
        return swap
