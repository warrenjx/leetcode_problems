class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)

        # get ascii sums of each string
        sum_1 = 0
        for i in range(m): 
            sum_1 += ord(s1[i])
        
        sum_2 = 0
        for i in range(n): 
            sum_2 += ord(s2[i])

        # find longest common subsequence (lcs)
        # dp holds the current lcs sum rather than character count of lcs
        dp = [[0] * (m + 1) for i in range(n + 1)]

        # generally same process as longst common substring
        for i in range(1, n + 1): 
            for j in range(1, m + 1): 
                if s1[j - 1] == s2[i - 1]: 
                    # add character ascii rather than 1
                    dp[i][j] = ord(s1[j - 1]) + dp[i - 1][j - 1]
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 

        # solution is sum_1 + sum_2 - 2 * lcs_sum 
        #   thats the ascii cost to remove all characters in s1, s2 that arent part of lcs
        #   it works because all terms in s1, s2 are characters so no large outliers are possible
        return sum_1 + sum_2 - (2 * dp[-1][-1])
