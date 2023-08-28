class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)

        # dp holds the minimum falling path sum at each point in matrix
        dp = [[0] * n for i in range(n)]

        # seed the first row
        for i in range(n): 
            # minimum path sum at this point is just the term at matrix[0][i]
            dp[0][i] = matrix[0][i]

        for i in range(1, n): 
            # minimum path sum is based off of the space directly above and 1 to the left
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + matrix[i][0]
            # minimum path sum is based off of the space directly above and 1 to the right
            dp[i][n - 1] = min(dp[i - 1][n - 1], dp[i - 1][n - 2]) + matrix[i][n - 1]

            # interior ones can be filled in with a loop
            for j in range(1, n - 1): 
                # minimum path sum is based off of the min of the 3 squares that can reach the current one
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
        
        return min(dp[n - 1])
