# ======================================
# LeetCode Problem: longest valid parentheses
# Language: python
# Link: https://leetcode.com/problems/longest-valid-parentheses/
# Synced by: LinkCode
# Date: 10/6/2026, 9:08:47 PM
# ======================================


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack = [-1]
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
                    
        return count