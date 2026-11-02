# ======================================
# LeetCode Problem: combination sum
# Language: python
# Link: https://leetcode.com/problems/combination-sum/
# Synced by: LinkCode
# Date: 11/2/2026, 8:42:05 PM
# ======================================


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        remaining=target
        final_res=[]
        res=[]
        
        def backtrack(strt_idx,remaining,res):
            n=len(candidates)
            if remaining==0:
                return final_res.append(res[:])
            if remaining<0:
                return
            for i in range(strt_idx, n):
                res.append(candidates[i])
                backtrack(i,remaining-candidates[i],res)
                res.pop()
        backtrack(0,remaining,res)
        return final_res