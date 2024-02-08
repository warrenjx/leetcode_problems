class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # squares is like the coins in the coin change problem
        squares = []
        idx = 1
        while idx ** 2 <= n: 
            squares.append(idx ** 2)

            idx += 1
        
        # dp[i] holds the least number of coins to get to i
        dp = [10001] * (n + 1)
        # 0 coins is the base case for recursion
        dp[0] = 0

        # go through squares at each number i
        for i in range(1, n + 1): 
            for sqr in squares: 
                if sqr == i: # if it is equal to a square
                    dp[i] = 1
                elif sqr > i: # squares are in sorted order
                    break
                else: # check if adding a coin can reduce the number of coins required
                    dp[i] = min(dp[i], dp[i - sqr] + 1)

        return dp[n]
