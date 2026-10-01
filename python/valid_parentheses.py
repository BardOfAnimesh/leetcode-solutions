# ======================================
# LeetCode Problem: valid parentheses
# Language: python
# Link: https://leetcode.com/problems/valid-parentheses/
# Synced by: LinkCode
# Date: 10/1/2026, 5:38:22 PM
# ======================================


class Solution(object):
    def isValid(self, s):
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                return False
        return not stack