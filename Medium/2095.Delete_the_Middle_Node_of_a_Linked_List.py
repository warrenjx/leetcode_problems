# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head 
        slow = head # slow pointer will be at the middle node
        prev = None # prev stores the node before slow

        # use fast and slow pointer to move pointers to right spots
        while fast: 
            fast = fast.next
            if fast: 
                fast = fast.next
            else: 
                break

            prev = slow
            slow = slow.next
    
        if slow and prev: # if not, there is no list return None
            prev.next = slow.next
        else: 
            return None

        return head
