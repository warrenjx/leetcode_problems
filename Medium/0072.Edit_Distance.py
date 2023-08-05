class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # convenience variables
        m = len(word1)
        n = len(word2)
        
        # dp holds the amount of operations to change word1 to word2 at i, j position
        dp = [[0] * (m + 1) for i in range(n + 1)]

        # manually fill in the first row and column
        # the number of operations to change empty to the other is just index + 1
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(1, n + 1): 
            dp[i][0] = i
        
        # main tabulation process
        for i in range(1, n + 1): 
            for j in range(1, m + 1): 
                if word1[j - 1] == word2[i - 1]: # character match means no operations necessary from prev diagonal
                    dp[i][j] = dp[i - 1][j - 1]
                else: # no match means 1 move over any of the previous ones
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
            
        return dp[n][m]
