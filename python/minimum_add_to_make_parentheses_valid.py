# ======================================
# LeetCode Problem: minimum add to make parentheses valid
# Language: python
# Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Synced by: LinkCode
# Date: 10/6/2026, 9:41:25 PM
# ======================================


class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        count=0
        for ch in s:
            if ch =="(":
                stack.append(ch)
                count+=1
            elif ch==")":
                if stack and stack[-1]=='(':
                    count-=1
                    stack.pop()
                
                elif not stack:
                    count+=1
        return count