# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # holds all the twin sums
        sums = []

        # fast and slow pointers
        fast = head
        slow = head

        # add first half of array to sums
        while fast: 
            sums.append(slow.val)

            fast = fast.next.next
            slow = slow.next
        
        # add the second half of array to sums
        for i in range(len(sums) - 1, -1, -1): 
            sums[i] += slow.val

            slow = slow.next
        
        return max(sums)
