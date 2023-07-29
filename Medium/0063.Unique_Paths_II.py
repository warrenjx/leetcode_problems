class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # edge case: obstacle blocks the start
        if obstacleGrid[0][0] == 1: 
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # each entry in dp array holds number of ways to get to a spot
        dp = [[0] * n for _ in range(m)]
        
        # populate top row
        for i in range(n): 
            if obstacleGrid[0][i] == 0: # only populate it if not obstacle
                dp[0][i] = 1
            else: # if obstacle cannot reach anywhere past it
                break
        
        # populate leftmost column
        for i in range(m): 
            if obstacleGrid[i][0] == 0: 
                dp[i][0] = 1
            else: 
                break
        
        for i in range(1, m): 
            for j in range(1, n): 
                # no paths to reach obstacle
                if obstacleGrid[i][j] == 1: 
                    continue

                if obstacleGrid[i][j - 1] == 1 and obstacleGrid[i - 1][j] == 1: # tile is fully blocked
                    # tile is completely blocked by obstacles
                    continue
                elif obstacleGrid[i][j - 1] == 1: # tile is blocked from the left
                    dp[i][j] = dp[i - 1][j]
                elif obstacleGrid[i - 1][j] == 1: # tile is blocked from above
                    dp[i][j] = dp[i][j - 1]
                else: # tile is not blocked at all, normal process
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]
