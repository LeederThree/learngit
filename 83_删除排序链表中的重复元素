# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        forward = head

        while forward.next:
            if forward.val == forward.next.val:
                forward.next = forward.next.next
            else:
                forward = forward.next
        return head
