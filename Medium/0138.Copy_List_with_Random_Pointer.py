"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # edge case handling
        if not head: 
            return None

        # create a deep copy of list        
        new_head = ListNode
        new_ptr = new_head

        # use hashtable to translate old nodes to new nodes for filling in random
        hashtable = {}

        # first add all the nodes with values
        ptr = head
        while ptr: 
            new_ptr.next = ListNode()
            new_ptr = new_ptr.next

            new_ptr.val = ptr.val
            
            # add info to hashtable for translating old to new nodes
            hashtable[ptr] = new_ptr

            #new_ptr.random = None

            ptr = ptr.next
        
        # traverse list and add all the random pointers
        ptr = head
        new_ptr = new_head
        while ptr: 
            new_ptr = new_ptr.next
            
            if ptr.random: 
                new_ptr.random = hashtable[ptr.random]
            else: 
                new_ptr.random = None
                
            ptr = ptr.next

        return new_head.next 
