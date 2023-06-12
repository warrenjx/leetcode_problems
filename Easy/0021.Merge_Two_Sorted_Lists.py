# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        ptr = ListNode()

        # merging the 2 linked lists
        head = ptr
        while list1 and list2: 
            if list1.val < list2.val: 
                ptr.next = ListNode(list1.val)
                list1 = list1.next
            else: 
                ptr.next = ListNode(list2.val)
                list2 = list2.next
            
            ptr = ptr.next
        
        # if any of the lists have any left, add them to end of merged list
        if list1: 
            ptr.next = list1
        elif list2: 
            ptr.next = list2

        return head.next
