# ======================================
# LeetCode Problem: valid parenthesis string
# Language: python
# Link: https://leetcode.com/problems/valid-parenthesis-string/
# Synced by: LinkCode
# Date: 10/4/2026, 10:32:01 PM
# ======================================


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_brack=0
        max_brack=0
        for ch in s:
            if ch in '(':
                min_brack+=1
                max_brack+=1
            elif ch in ')':
                min_brack-=1
                max_brack-=1
            elif ch in "*":
                min_brack-=1
                max_brack+=1
                    
            if min_brack<0:
                min_brack=0
            if max_brack<0:
                return False
        if  min_brack!=0:
            return False
        return True