# ======================================
# LeetCode Problem: count servers that communicate
# Language: python
# Link: https://leetcode.com/problems/count-servers-that-communicate/
# Synced by: LinkCode
# Date: 11/9/2026, 12:21:09 AM
# ======================================


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        com_serv=0
        
        m=len(grid)
        n=len(grid[0])

        row_cnt=[0]*m
        col_cnt=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    row_cnt[i]+=1
                    col_cnt[j]+=1
                    
        for i in range(m):    
            for j in range(n):
                if grid[i][j]==1:
                    if row_cnt[i] > 1 or col_cnt[j]>1:
                        com_serv += 1

        return com_serv