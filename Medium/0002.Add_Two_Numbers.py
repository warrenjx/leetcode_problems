# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0

        # convert list1 to integer
        order = 1
        while l1: 
            num1 += l1.val * order

            l1 = l1.next
            order *= 10

        # convert list2 to integer
        order = 1
        while l2: 
            num2 += l2.val * order

            l2 = l2.next
            order *= 10
        
        sol = num1 + num2
        
        # take care of edge case where nothing will be returned if sol == 0
        if sol == 0: 
            return ListNode(0)

        ptr = ListNode()
        # keep head pointer to return later
        head = ptr
        
        # convert sol back into a list
        while sol > 0: 
            ptr.next = ListNode(sol % 10)

            sol /= 10
            ptr = ptr.next
        
        return head.next
