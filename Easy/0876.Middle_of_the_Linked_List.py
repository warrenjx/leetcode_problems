# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        # fast and slow pointer
        while fast: 
            fast = fast.next
            if fast: 
                fast = fast.next
            else: 
                break
            
            head = head.next
        
        return head
