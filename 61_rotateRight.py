# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        n = 1
        while p.next:
            p = p.next
            n += 1
        p.next = head
        for i in range(n-k%n):
            p = p.next
        head = p.next
        p.next = None
        return head
