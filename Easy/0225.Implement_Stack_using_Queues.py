class MyStack(object):

    def __init__(self):
        # one queue is used to hold items, other is used to hold the terms when popping
        self.q_1 = deque()
        self.q_2 = deque()
        self.len = 0 # length of the stack
        self.is_1 = True # denotes which queue is the buffer and which has the data

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.is_1: # append is simple, just to the active queue
            self.q_1.append(x)
        else: 
            self.q_2.append(x)
        
        self.len += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.is_1: 
            # first pop all of the terms except last term into the other queue
            for i in range(self.len - 1): 
                self.q_2.append(self.q_1.popleft())
            
            self.len -= 1 # decrement length
            self.is_1 = False # set other queue as active, current is buffer

            return self.q_1.popleft() # last term of queue was the first one on
        else: 
            for i in range(self.len - 1): 
                self.q_1.append(self.q_2.popleft())
            
            self.len -= 1
            self.is_1 = True
            
            return self.q_2.popleft()
        
    def top(self):
        """
        :rtype: int
        """
        if self.is_1: # return the end of the active queue
            return self.q_1[self.len - 1]
        else: 
            return self.q_2[self.len - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
