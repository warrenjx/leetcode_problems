# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # find the overall length of list
        length = 0
        ptr = head
        while ptr: 
            length += 1
            ptr = ptr.next
        
        # take care of edge cases: 
        if length == 1: # only 1 node
            return None
        elif length - n == 0: # first node
            return head.next
        
        # get pointer to node before the deleted
        ptr = head
        for i in range(length - n - 1): 
            ptr = ptr.next
        
        # remove nth node
        ptr.next = ptr.next.next

        return head
