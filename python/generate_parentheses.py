# ======================================
# LeetCode Problem: generate parentheses
# Language: python
# Link: https://leetcode.com/problems/generate-parentheses/
# Synced by: LinkCode
# Date: 10/13/2026, 11:05:44 PM
# ======================================


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        s=''
        ope=0
        clo=0
        def backtrak(ope,clo,s,n):
            if ope==n and clo==n:
                return result.append(s)
            
            if ope<=n:
                
                
                backtrak(ope+1,clo,s+'(',n)
            if clo<ope:
                
                backtrak(ope,clo+1,s+')',n)
        
        backtrak(ope,clo,s,n)
        return result 
        


        