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
        pA = headA
        pB = headB

        while pA or pB:
            if pA == pB:
                return pA 
            if not pA:
                pA = headB
            else: pA = pA.next
            if not pB:
                pB = headA
            else: pB = pB.next                   
        return None
