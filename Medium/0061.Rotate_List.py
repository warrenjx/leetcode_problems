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
        # edge case: no nodes
        if not head: 
            return None 

        # get total length of list and the current tail which will be used for reconstruction
        old_tail = head
        ct = 1
        while old_tail.next: 
            ct += 1

            old_tail = old_tail.next

        # edge cases
        if k % ct == 0: # k is divisible by count, no need to do rotations
            return head
        elif ct < k: # k is more than ct, trim it to less, get rid of excess rotations
            k %= ct

        # find where the new head will be
        old_head = head
        for i in range(ct - k): 
            head = head.next
        
        # extract the part of the list that needs to be rotated around
        temp = old_head
        for i in range(ct - k - 1): 
            temp = temp.next
        
        # cut off the part of list to avoid cycles
        temp.next = None
        
        # set cut section to its place
        old_tail.next = old_head

        return head
