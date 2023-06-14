# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # takes care of 0 and 1 node testcases
        if not head:
            return None
        elif not head.next: 
            return head
        
        # get the first 2 nodes ready for swapping
        curr = head.next
        prev = head
        prev.next = None

        # iteratively swap the direction of links in list
        while curr: 
            nex = curr.next

            curr.next = prev

            prev = curr
            curr = nex
        
        return prev
