# ======================================
# LeetCode Problem: find the index of the first occurrence in a string
# Language: python
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Synced by: LinkCode
# Date: 10/8/2026, 11:08:30 PM
# ======================================


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            index=haystack.index(needle)
            if index>=0:
                
                return index
        except Exception as e:
            return -1

        