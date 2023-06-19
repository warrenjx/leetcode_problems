class ListNode: 
    # doubly linked list
    def __init__(self, key, value): 
        self.key = key
        self.val = value
        self.pre = None
        self.nex = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashmap = {}
        self.cap = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        # make it circular, reduces overhead
        self.head.nex = self.tail
        self.tail.pre = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap: 
            node = self.hashmap[key]

            # move to front of list as it was just used
            self.remove_from_list(node)
            self.insert_at_head(node)

            return node.val
        else: 
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap: 
            # similar to get, but update value rather than return
            node = self.hashmap[key]

            self.remove_from_list(node)
            self.insert_at_head(node)

            node.val = value
        else: 
            # delete tail if out of space
            if len(self.hashmap) >= self.cap: 
                self.remove_from_tail()
            
            # just add new node at head
            node = ListNode(key, value)
            self.hashmap[key] = node
            self.insert_at_head(node)
    

    def remove_from_list(self, node): 
        # remove node from its place in list
        node.pre.nex = node.nex
        node.nex.pre = node.pre

    
    def insert_at_head(self, node): 
        # insert new node into place
        next_head = self.head.nex
        self.head.nex = node
        node.pre = self.head
        node.nex = next_head
        next_head.pre = node

    
    def remove_from_tail(self): 
        # if no terms just do nothing
        if len(self.hashmap) == 0: 
            return
        
        # find term to remove
        next_tail = self.tail.pre

        # remove term from hashmap and list
        del self.hashmap[next_tail.key]
        self.remove_from_list(next_tail)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
