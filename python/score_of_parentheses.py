# ======================================
# LeetCode Problem: score of parentheses
# Language: python
# Link: https://leetcode.com/problems/score-of-parentheses/
# Synced by: LinkCode
# Date: 10/5/2026, 9:07:48 PM
# ======================================


class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth=0
        count=0
        for i in range(len(s)):
            if s[i] in "(":
                depth+=1
            elif s[i] in ")":
                depth-=1
                if s[i-1]=="(" :
                    count+=2**depth
        return count