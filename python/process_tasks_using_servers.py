# ======================================
# LeetCode Problem: process tasks using servers
# Language: python
# Link: https://leetcode.com/problems/process-tasks-using-servers/
# Synced by: LinkCode
# Date: 11/7/2026, 10:46:39 PM
# ======================================


class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        aval_serv=sorted((w,i)for i,w in enumerate(servers))
        busy=[]
        ans=[0]*len(tasks)
        heapq.heapify(aval_serv)
        t=0

        for j,task_tm in enumerate(tasks):
            t=max(t,j)
            if not aval_serv:
                t=busy[0][0]
            while busy and busy[0][0]<=t:
                free_time, w, i = heapq.heappop(busy)
                heapq.heappush(aval_serv, (w, i))
            w,i=heapq.heappop(aval_serv)
            ans[j]=i
            heapq.heappush(busy, (t + task_tm, w, i))
        return ans