class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # convenience variables
        m = len(s)
        n = len(p)

        # each entry in dp represents if position at i in p and j in s can be reached
        dp = [[False] * (m + 1) for i in range(n + 1)]
        # seed start
        dp[0][0] = True
        # seed first column to deal with * 0 matches
        for i in range(1, n + 1): 
            if p[i - 1] == '*': 
                dp[i][0] = True
            else: 
                break

        # tabulation approach
        for i in range(1, n + 1): 
            for j in range(1, m + 1): 
                # pattern match cases
                if p[i - 1] == '*': # * case, matches any sequence, including none
                    # (i - 1) is vertical match, (both) is character match, (j - 1) is repeated match
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1] or dp[i][j - 1]
                elif p[i - 1] == '?' or p[i - 1] == s[j - 1]: # matches any char or if char is match
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]
