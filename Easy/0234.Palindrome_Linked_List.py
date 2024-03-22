# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # read all of the list terms into a double ended queue
        l = deque()
        while head: 
            l.append(head.val)
            head = head.next

        # check if it is a palindrome
        while l:
            if len(l) == 1: 
                break
            elif l[0] != l[-1]:
                return False

            l.pop()
            l.popleft() 

        return True
