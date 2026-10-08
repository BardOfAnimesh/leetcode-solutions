# ======================================
# LeetCode Problem: remove outermost parentheses
# Language: python
# Link: https://leetcode.com/problems/remove-outermost-parentheses/
# Synced by: LinkCode
# Date: 10/8/2026, 10:31:40 PM
# ======================================


class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        brack_str=''
        depth=0
        for ch in s:
            if ch=="(":
                depth+=1
                if depth>1:
                    brack_str=brack_str+"("
            elif ch==")":
                if depth>1:
                    brack_str=brack_str+")"
                depth-=1
            
            
                    
        return brack_str