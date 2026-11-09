# ======================================
# LeetCode Problem: find servers that handled most number of requests
# Language: python
# Link: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Synced by: LinkCode
# Date: 11/9/2026, 10:22:37 PM
# ======================================


class Solution(object):
    import heapq 
    from sortedcontainers import SortedList
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        free_serv=SortedList(range(k))
        busy=[]
        count=[0]*k
        for i,(arr,dur) in enumerate(zip(arrival,load)):
            while busy and busy[0][0]<=arr:
                _,serv_id=heapq.heappop(busy)
                free_serv.add(serv_id)
            
            if not free_serv:
                continue
            target=i%k
            idx = free_serv.bisect_left(target)
            
            if idx <len(free_serv):
                assigned_server=free_serv.pop(idx)
            else:
                assigned_server=free_serv.pop(0)

            count[assigned_server] += 1
            heapq.heappush(busy,(arr+dur, assigned_server))

        max_handled = max(count)
        return [s for s in range(k) if count[s] == max_handled]