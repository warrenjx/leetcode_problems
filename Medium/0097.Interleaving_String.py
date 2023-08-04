class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # convenience variables
        m = len(s1)
        n = len(s2)
        o = len(s3)

        # edge case: not enough or too many characters at all
        if m + n != o: 
            return False
        
        # initialize tabulation array
        dp = [[False] * (m + 1) for i in range(n + 1)]
        # seed the starting position
        dp[0][0] = True

        # fill in first row manually (matching s3 with s1 only)
        for i in range(1, m + 1): 
            if dp[0][i - 1] and s1[i - 1] == s3[i - 1]: 
                dp[0][i] = True
        # fill in first col manually (matching s3 with s2 only)
        for i in range(1, n + 1): 
            if dp[i - 1][0] and s2[i - 1] == s3[i - 1]: 
                dp[i][0] = True
        
        # main algorithm
        for i in range(1, n + 1): 
            for j in range(1, m + 1):
                # check if you can continue matching with s3 at any position
                if dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]: # have -1 because loop starts at 1
                    dp[i][j] = True
                if dp[i][j - 1] and s1[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True
        
        # last position of dp represents the reachability of the last character of s3
        return dp[n][m]
