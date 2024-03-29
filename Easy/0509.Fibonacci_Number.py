class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fibs = [0, 1]

        for i in range(2, n + 1): 
            fibs.append(fibs[i - 1] + fibs[i - 2])

        return fibs[n]
