# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: # edge case: no nodes
            return None
        elif not head.next or not head.next.next: # edge case: only 1 or 2 nodes
            return head

        odd = head # points to the head of the continuous odd section
        even = head.next # points to the head of the continuous even section

        # iterate over the list up to the last node if odd
        while even and even.next and even.next.next: 
            # save the next even and odd pointer locations
            n_even = even.next.next 
            n_odd = even.next

            # swap odd after even to after odd pointer
            swap = even.next
            odd_next = odd.next

            odd.next = swap
            swap.next = odd_next
            even.next = n_even

            # set new even and odd positions
            even = n_even
            odd = n_odd

        # add last node to appropriate position if odd number
        if even.next: 
            last = even.next

            even.next = None

            last.next = odd.next
            odd.next = last

        return head
