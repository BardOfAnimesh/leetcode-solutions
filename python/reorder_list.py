# ======================================
# LeetCode Problem: reorder list
# Language: python
# Link: https://leetcode.com/problems/reorder-list/
# Synced by: LinkCode
# Date: 10/7/2026, 7:50:52 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            prev=slow

        curr=slow.next
        prev=None
        slow.next=prev

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr= next_node

        curr=head
        while prev:
            temp=curr.next
            curr.next=prev
            temp2=prev.next
            prev.next=temp
            curr=temp
            prev=temp2
        
        return head