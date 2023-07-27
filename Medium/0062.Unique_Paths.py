class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # initialize dp array: each position is the amount of paths to get to the point
        dp = [[0] * n for _ in range(m)]

        # initialize top row of grid
        for i in range(n): 
            dp[0][i] = 1

        # initialize leftmost column of grid
        for i in range(m): 
            dp[i][0] = 1

        # do the dp to fill in everything else
        for i in range(1, m): 
            for j in range(1, n): 
                # each square is just a combination of the previous squares
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
