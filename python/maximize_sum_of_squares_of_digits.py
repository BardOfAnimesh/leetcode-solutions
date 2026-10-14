# ======================================
# LeetCode Problem: maximize sum of squares of digits
# Language: python
# Link: https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
# Synced by: LinkCode
# Date: 10/14/2026, 7:16:28 PM
# ======================================


class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum> num*9:
            return ""

        res_str=''
        
        k=sum//9
        remain=sum%9
        for j in range(k):
            res_str=res_str+'9'
        for i in range(num-k):

            if remain==0:
                res_str=res_str+'0'
            elif remain!=0:
                res_str=res_str+str(remain)
                remain=0
        return res_str