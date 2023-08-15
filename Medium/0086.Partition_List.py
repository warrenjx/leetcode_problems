# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # create 2 lists, 1 representing the under and over x lists
        under = ListNode(-1)
        over = ListNode(-1)
        # pointers which will be used to iterate over them
        under_head = under
        over_head = over

        # iteratively fill the lists
        while head: 
            if head.val < x: 
                under.next = head
                under = under.next
            else: 
                over.next = head
                over = over.next
            
            head = head.next
        
        # attach over list to end of under list
        under.next = over_head.next
        # trim end of over list to avoid cycles
        over.next = None

        # return head next because head is a placeholder
        return under_head.next
