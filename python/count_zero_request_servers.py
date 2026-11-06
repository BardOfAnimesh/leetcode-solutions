# ======================================
# LeetCode Problem: count zero request servers
# Language: python
# Link: https://leetcode.com/problems/count-zero-request-servers/
# Synced by: LinkCode
# Date: 11/6/2026, 11:16:19 PM
# ======================================


class Solution(object):
    from collections import defaultdict
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        indx_tm_queries=sorted((q,i) for i,q in enumerate(queries))
        logs.sort(key= lambda logs:logs[1])
        ans=[0]*len(queries)
        left,right=0,0
        active_servers=0
        cnt=defaultdict(int)

        for q_time, original_idx in indx_tm_queries:
            while right<len(logs) and logs[right][1]<=q_time:
                server=logs[right][0]
                if cnt[server] == 0:
                    active_servers+=1
                cnt[server]+=1
                right+=1
            while left < len(logs) and logs[left][1] < q_time - x:
                server = logs[left][0]
                cnt[server]-=1
                if cnt[server] == 0:
                    active_servers-=1
                left+=1
            ans[original_idx] = n-active_servers
        return ans