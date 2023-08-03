class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # convenience variables
        m = len(matrix)
        n = len(matrix[0])

        # dp array holds the longest path at each point in matrix
        # -1 is placeholder, when not -1 it is already been calculated
        dp = [[-1] * n for i in range(m)]
        
        # recursive dfs function
        def dfs(y, x): 
            # memoization condition
            if dp[y][x] != -1: 
                return dp[y][x]
            
            # base path length
            curr = 1
            # visit neighbors
            if y > 0 and matrix[y][x] < matrix[y - 1][x]: 
                curr = max(curr, dfs(y - 1, x) + 1)
            if y < m - 1 and matrix[y][x] < matrix[y + 1][x]: 
                curr = max(curr, dfs(y + 1, x) + 1)
            if x > 0 and matrix[y][x] < matrix[y][x - 1]: 
                curr = max(curr, dfs(y, x - 1) + 1)
            if x < n - 1 and matrix[y][x] < matrix[y][x + 1]: 
                curr = max(curr, dfs(y, x + 1) + 1)
            
            # set array value to maximum path length
            dp[y][x] = curr
            
            return curr

        # dfs every node in matrix to find longest path
        longest = 0
        for i in range(m): 
            for j in range(n): 
                if dp[i][j] == -1: 
                    longest = max(longest, dfs(i, j))
        
        return longest
