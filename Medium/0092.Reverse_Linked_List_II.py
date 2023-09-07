# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # only 1 node in partition, no need to do anything
        if left == right: 
            return head
        
        if left == 1: # separate case for if partition starts at beginning
            tail = head

            # same code as reverse linked list 1 pretty much
            prev = None
            ptr = head
            for i in range(right - left + 1): 
                temp = ptr.next
                ptr.next = prev

                prev = ptr
                ptr = temp
            
            tail.next = ptr

            return prev

        # prev_left is the term before the term at left, will be connected to right term
        prev_left = head
        for i in range(left - 2): 
            prev_left = prev_left.next

        # tail is the first term in the reversed section
        tail = prev_left.next
        
        # reverse the refersed section
        ptr = tail
        prev = None
        for i in range(right - left + 1): 
            temp = ptr.next
            ptr.next = prev

            prev = ptr
            ptr = temp

        # connect the reversed section to the new section
        
        prev_left.next = prev
        tail.next = ptr        

        return head
