class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []
        self.curr_min = 2147483647 # INT max from C

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val <= self.curr_min: # <= not < so you get proper chain of mins
            self.mins.append(self.curr_min)
            self.curr_min = val
        
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        popped = self.stack.pop()
        
        if popped == self.curr_min: 
            self.curr_min = self.mins.pop()
        
        return popped

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.curr_min # separate variable makes it easier for this func
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()