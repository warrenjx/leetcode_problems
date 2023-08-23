class RecentCounter(object):

    def __init__(self):
        # all the init needs is a queue
        self.q = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # add current task
        self.q.append(t)

        # remove all tasks older than 3000 ms
        while self.q[0] < t - 3000: 
            self.q.popleft()

        # len of q is the amount of recent calls
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
