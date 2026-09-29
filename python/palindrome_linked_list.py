# ======================================
# LeetCode Problem: palindrome linked list
# Language: python
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Synced by: LinkCode
# Date: 9/30/2026, 12:29:07 AM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        fast=head
        slow=head
        count=0
        while slow:
            if fast and fast.next:
            
                fast=fast.next.next
                prev=slow
                slow=slow.next
            else:
                next_node=slow.next
                slow.next=prev
                prev=slow
                slow=next_node
                count+=1
        
        slow =prev

        curr=head

        while count:
            if curr.val==slow.val:
                curr=curr.next
                slow=slow.next
                count-=1
            else:
                return False
        return True
