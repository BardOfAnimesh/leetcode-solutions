# ======================================
# LeetCode Problem: minimum insertions to balance a parentheses string
# Language: python
# Link: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# Synced by: LinkCode
# Date: 10/10/2026, 1:09:33 AM
# ======================================


class Solution(object):

    def minInsertions(self, s):
        """
        :type s: str

        :rtype: int
        """
        insert = 0
        close_paran=0

        for ch in s:
            if ch == "(":
                if close_paran%2!= 0:
                    insert += 1
                    close_paran-= 1

                close_paran+= 2

            elif ch == ")":
                close_paran -= 1
                if close_paran == -1:
                    insert+= 1
                    close_paran=1

        return insert+close_paran