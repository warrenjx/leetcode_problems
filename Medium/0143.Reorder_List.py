# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # back pointer ends up being at the head of 2nd half of list
        fast = head
        back = head
        prev = None
        while fast: 
            fast = fast.next
            if fast: 
                fast = fast.next
            
            prev = back

            back = back.next
        
        # cut off lsit after the first half
        prev.next = None

        # reverse the back half of list
        back = self.reverse_list(back)

        # merge front half and reversed back half
        self.merge_list(head, back)

    
    # reverses the linked list
    def reverse_list(self, head): 
        prev = None
        cur = head

        while cur: 
            nex = cur.next

            cur.next = prev

            prev = cur
            cur = nex
        
        return prev
    
    
    # merges linked list by every other term
    def merge_list(self, l1, l2): 
        side = True

        while l1 and l2: 
            if side: 
                nex_l1 = l1.next
                l1.next = l2
                l1 = nex_l1
                
                side = False
            else: 
                nex_l2 = l2.next
                l2.next = l1
                l2 = nex_l2

                side = True
