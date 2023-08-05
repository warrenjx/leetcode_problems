class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # create parsed version p to better deal with * cases
        p_p = []
        
        # fill list in backwards for convenience
        i = len(p) - 1
        while i >= 0: 
            if p[i] == '*': # bundle * with the char its modifying
                p_p.insert(0, p[i - 1:i + 1])
                i -= 1
            else: 
                p_p.insert(0, p[i])
            
            i -= 1
        
        # convenience variables
        n = len(s)
        m = len(p_p)

        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True # seeding a char match
        # seeding for * 0 matches
        for i in range(1, m + 1): 
            if p_p[i - 1][-1] == '*':
                dp[i][0] = True
            else: 
                break

        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                # * match cases
                if p_p[i - 1][-1] == '*': 
                    if p_p[i - 1][0] == s[j - 1] or p_p[i - 1][0] == '.': # character match, 1 or more repetition
                        # * matches al; 3 cases
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j - 1] or dp[i - 1][j]
                    else: # no match, 0 repetition
                        dp[i][j] = dp[i - 1][j]

                # . and char match cases
                elif p_p[i - 1] == '.' or p_p[i - 1] == s[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
