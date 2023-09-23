class StockSpanner(object):

    def __init__(self):
        self.d = 1 # the current day
        self.s = deque() # stack holding (value, day) pairs


    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = -1 # initialize span variable

        while self.s and price >= self.s[-1][0]: # pop any prices that are less than or greater than the current
            self.s.pop()
        
        if self.s: # if a greater stock is found, span is to that stock price
            span = self.d - self.s[-1][1]
        else: # no greater stock found, span is current day 
            span = self.d
        
        self.s.append((price, self.d)) # add price to stack

        self.d += 1 # incrememnt current day for next iteration
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
