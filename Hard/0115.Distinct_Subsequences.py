class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # convenience variables
        m = len(s)
        n = len(t)

        # dp holds the amount of subsequences at a certain position in s, t
        dp = [[0] * (m + 1) for i in range(n + 1)]
        # seed the first row of dp with 1s
        # there is 1 way to make empty sequence no matter how many chars you have
        for i in range(m + 1): 
            dp[0][i] = 1

        # main tabulation process
        for i in range(1, n + 1): 
            for j in range(1, m + 1): 
                if s[j - 1] == t[i - 1]: # character match
                    # new sol is the combination of both previous solutions before the new char
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else: # no character match
                    # propagate the solution to previous iteration without newest char
                    dp[i][j] = dp[i][j - 1]

        return dp[n][m]
