# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # count the total length of the list
        ptr = head
        ct = 0
        while ptr: 
            ptr = ptr.next
            ct += 1
        
        # lens holds the length of each subarray
        lens = [ct // k] * k
        # add 1 to each length for every extra if it doesn't divide evenly
        leftovers = ct % k
        for i in range(leftovers): 
            lens[i] += 1
        
        sol = [None for i in range(k)]
        
        # separate the list into the sections
        ptr = head
        for i in range(min(len(lens), ct)): 
            sol[i] = ptr # set solution to current pointer

            # traverse down the list 
            for i in range(lens[i] - 1): 
                ptr = ptr.next

            # cut the list off and move to next partition
            temp = ptr.next
            ptr.next = None
            ptr = temp

        return sol
