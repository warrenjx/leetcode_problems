class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        # format: dp[i][j] = amount of profit on i-th day and j represents if you bought (1) or sold (0)
        dp = [[-1] * 2 for i in range(n + 1)]

        # starting terms
        dp[0][0] = 0 # no buying or selling
        dp[0][1] = -999 # negative placeholder because first buy will be negative

        for i in range(1, n + 1): 
            # buying/resting position: 
            # dp[i][0] is the max of either resting (previous entry) or selling a previous buy
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])

            # selling position: 
            if i == 1: # if i == 1, only thing to do is to buy stock
                dp[i][1] = max(dp[i - 1][1], -prices[i - 1])
            else: # else, can either hold current stock or sell at 2 places ago (because of cooldown)
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])
        
        # cannot hold stock on last day so must be dp[i][0]
        return dp[-1][0]
