class MyQueue(object):

    def __init__(self):
        # stack to be filled when you need to read
        self.read = deque()
        # stack that gets pushed to
        self.write = deque()

        # length for convenience
        self.length = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # simply just push to write stack
        self.write.append(x)
        self.length += 1
        

    def pop(self):
        """
        :rtype: int
        """
        # decrement length
        self.length -= 1

        # store all terms besides desired term on read stack
        for i in range(self.length): 
            self.read.append(self.write.pop())

        # store solution term
        sol = self.write.pop()

        # move terms from read back to write stack
        for i in range(self.length): 
            self.write.append(self.read.pop())

        return sol

    def peek(self):
        """
        :rtype: int
        """
        return self.write[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.length == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
