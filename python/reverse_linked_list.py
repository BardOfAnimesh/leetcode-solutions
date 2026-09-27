# ======================================
# LeetCode Problem: reverse linked list
# Language: python
# Link: https://leetcode.com/problems/reverse-linked-list/
# Synced by: LinkCode
# Date: 9/27/2026, 11:12:22 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev= None 
        curr=head

        while  curr is not None:
            next_node = curr.next

            curr.next = prev

            prev =curr

            curr=next_node
        
        return prev