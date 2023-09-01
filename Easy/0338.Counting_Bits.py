class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # holds the amount of bits in index
        dp = [0] * (n + 1)

        # start at 1 since 0 is the default value at 0
        for i in range(1, n + 1): 
            # i shares all the same bits as (i >> 1) except for the LSB
            # the LSB is determined if i is odd or not hence (i % 2)
            dp[i] = dp[i >> 1] + (i % 2)

        return dp
