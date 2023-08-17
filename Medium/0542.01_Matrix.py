class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # convenience variables
        m = len(mat)
        n = len(mat[0])

        # dp holds the distance from the nearest 0 for each cell
        dp = [[0] * n for i in range(m)]

        # first iterate starting from 0
        for i in range(m): 
            for j in range(n): 
                # if a term is a 1, will have nonzero distance
                if mat[i][j] == 1: 
                    dp[i][j] = 999999
                
                # since starting from 0, can only accurately get distances from up and left
                if i > 0: 
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j > 0: 
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

        # next iterate starting from n/m
        for i in range(m - 1, -1, -1): 
            for j in range(n - 1, -1, -1):
                # can accurately get distances from down and right starting from the top 
                if i < m - 1: 
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1: 
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)

        return dp
