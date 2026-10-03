# ======================================
# LeetCode Problem: intersection of two linked lists
# Language: python
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Synced by: LinkCode
# Date: 10/3/2026, 6:34:28 PM
# ======================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lst1= headA
        lst2=headB
        counta=0
        countb=0
        while (lst1) or (lst2):
            if lst1 != None:
                lst1=lst1.next
                counta+=1
            if lst2 !=None:
                lst2=lst2.next
                countb+=1
        cal1=0
        cal2=0
        if counta>countb:
            cal1=counta-countb

        elif countb>counta:
            cal2=countb-counta

        lst1= headA
        lst2=headB

        while (lst1) and (lst2):
            if lst1==lst2:
                return lst1
            if cal1>0:
                lst1=lst1.next
                cal1-=1
            elif cal2>0:
                lst2=lst2.next
                cal2-=1
            else:
                lst1=lst1.next
                lst2=lst2.next
                
        
        return None