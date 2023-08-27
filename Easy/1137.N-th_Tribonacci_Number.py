class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp holds fibonnaci number of index
        dp = [0] * max(3, n + 1)

        # seed the initial numbers
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # fill in the rest
        for i in range(3, n + 1): 
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
