# ======================================
# LeetCode Problem: remove nth node from end of list
# Language: python
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Synced by: LinkCode
# Date: 10/1/2026, 6:59:19 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        slow=dummy
        fast=dummy
        i=0
        while fast.next:
            if i<n:
                fast=fast.next
                i+=1
            else:
                slow=slow.next
                fast=fast.next
        
        slow.next=slow.next.next
        return dummy.next
        
