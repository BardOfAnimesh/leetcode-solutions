# ======================================
# LeetCode Problem: minimum sum of squared difference
# Language: python
# Link: https://leetcode.com/problems/minimum-sum-of-squared-difference/
# Synced by: LinkCode
# Date: 10/12/2026, 12:04:33 AM
# ======================================


class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        from collections import Counter
        lst1=[]
        K=k1+k2
        

        for i in range(len(nums1)):
            lst1.append(abs(nums1[i]-nums2[i]))
        
        if sum(lst1) <= K:
            return 0

        tally=Counter(lst1)
        low=0
        high=max(lst1)
        best_mid=high

        while low<=high:
            mid=(low+high)//2

            cost = sum(max(0, d - mid) for d in lst1)

            if cost<=K:
                best_mid=mid
                high=mid-1
            else:
                low=mid+1

        
       
        spent = 0
        for d in list(tally.keys()):
            if d > best_mid:
                excess = d - best_mid
                count = tally[d]
                spent += excess * count
                tally[best_mid] += count
                tally[d] = 0
        
        leftover = K - spent
        if leftover > 0 and best_mid > 0:
            drop_count=min(leftover, tally[best_mid])
            tally[best_mid]-=drop_count
            tally[best_mid - 1]+=drop_count
        
        return sum(d * d * count for d, count in tally.items())