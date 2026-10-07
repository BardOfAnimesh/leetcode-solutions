# ======================================
# LeetCode Problem: remove invalid parentheses
# Language: python
# Link: https://leetcode.com/problems/remove-invalid-parentheses/
# Synced by: LinkCode
# Date: 10/8/2026, 12:18:58 AM
# ======================================


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        balance=0
        extra_open=0
        extra_close=0
        result=[]
        curr_str=''
        index=0
        for i,ch in enumerate(s):
            if ch =='(':
                balance+=1
            elif ch ==')':
                if balance>0:
                    balance-=1
                else:
                    extra_close+=1
            

        extra_open=balance

        
        def backtrack(index, balance, extra_open, extra_close, curr_str):
            
            if index==len(s):
                if extra_open==0 and extra_close==0 and balance==0:
                    if curr_str not in result:
                        result.append(curr_str)
                return
            
            ch = s[index]
            if ch not in "()":
                backtrack(index+1, balance, extra_open, extra_close, curr_str+ch)
            elif ch =='(':
                if extra_open>0:#I'm using it to remove (
                    backtrack(index+1, balance, extra_open-1, extra_close, curr_str)
                    
                backtrack(index+1, balance+1, extra_open, extra_close, curr_str+ch)#to keep (
            
            elif ch==')':
                if extra_close>0:
                    backtrack(index+1, balance, extra_open, extra_close-1, curr_str)
                if balance>0:    
                    backtrack(index+1, balance-1, extra_open, extra_close, curr_str+ch)
                
        #function ke dako
        backtrack(index, 0, extra_open, extra_close, curr_str)

        return result