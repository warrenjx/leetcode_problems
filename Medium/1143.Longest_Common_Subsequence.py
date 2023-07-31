class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)

        # dp holds the maximum common subsequence at that position
        # is len + 1 for simplicity (rather than making first row and column manually)
        dp = [[0] * (m + 1) for i in range(n + 1)]

        # calculate every subproblem leading up to actual solution
        for i in range(1, n + 1): 
            for j in range(1, m + 1): 
                # same cases as the recursive solution
                if text1[j - 1] == text2[i - 1]: # if a matching character is found
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else: # no matching character, propagate previous solutions
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # since started iterating from beginning, ans is at end of dp
        return dp[-1][-1]
