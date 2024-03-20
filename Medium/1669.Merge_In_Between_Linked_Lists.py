# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # pointers represent the start and end of the removed portion of list1
        start = None
        end = list1
        # pointers are the previous nodes to start and end nodes
        s_prev, e_prev = None, None

        # position start and end nodes
        for i in range(b + 1): 
            if i == a: 
                s_prev = e_prev
                start = end

            # need this when a == b
            if i == b: 
                break

            e_prev = end
            end = end.next

        # replace start node with list2
        s_prev.next = list2

        # move pointer through list2
        ptr = list2
        while ptr.next: 
            ptr = ptr.next

        # put rest of list1 after list2
        ptr.next = end.next

        # change was done in place
        return list1
