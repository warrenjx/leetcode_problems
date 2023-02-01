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
        
        # find numerical value of sum
        num = self.list_to_num(l1) + self.list_to_num(l2)
        
        # iteratively turn numerical value into linked list of desired format
        sol = ListNode()
        temp = sol
        
        temp.val = num % 10
        num /= 10
        
        while num > 0: 
            temp.next = ListNode()
            temp = temp.next
            
            temp.val = num % 10
            
            num /= 10
            
        return sol
    
    # function turns linked list into decimal digit
    def list_to_num(self, head): 
        num = 0
        mag = 1

        while head: 
            num += (head.val % 10) * mag

            mag *= 10
            head = head.next
        
        return num