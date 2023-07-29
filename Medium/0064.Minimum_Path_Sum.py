class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) # y-axis
        n = len(grid[0]) # x-axis

        dp = [[-1] * n for _ in range(m)]

        # populate the beginning of dp so main algorithm can work
        dp[0][0] = grid[0][0]

        # populate top row
        for i in range(1, n): 
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        # populate leftmost column
        for i in range(1, m): 
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # each entry in dp represents the lowest cost way to get to it
        for i in range(1, m): 
            for j in range(1, n): 
                # take minimum of the only squares that can reach it plus current cost
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
