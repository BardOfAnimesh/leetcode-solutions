# ======================================
# LeetCode Problem: linked list cycle ii
# Language: python
# Link: https://leetcode.com/problems/linked-list-cycle-ii/
# Synced by: LinkCode
# Date: 10/3/2026, 6:33:07 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow= head
        fast = head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break

        if not fast or not fast.next:
            return None
        
        slow=head

        while slow!= fast:
            slow=slow.next
            fast=fast.next
        
        return slow
        