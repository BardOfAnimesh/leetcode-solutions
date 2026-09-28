# ======================================
# LeetCode Problem: remove duplicates from sorted list
# Language: python
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Synced by: LinkCode
# Date: 9/29/2026, 12:36:03 AM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        curr=head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next=curr.next.next
            elif curr.val!=curr.next.val:
                curr=curr.next
            else:
                break
                
        return head

