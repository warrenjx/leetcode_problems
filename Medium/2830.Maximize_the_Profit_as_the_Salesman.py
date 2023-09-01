class Solution(object):
    def maximizeTheProfit(self, n, offers):
        """
        :type n: int
        :type offers: List[List[int]]
        :rtype: int
        """
        # ints maps ending indeces to their start and gold
        ints = [[] for i in range(n)]
        # populate ints
        for s, e, g in offers: 
            ints[e].append((s, g))
        
        # dp holds maximum money you can buy at each index
        dp = [0] * (n + 1)
        # start from 1 as 0 is default value
        for i in range(1, n + 1): 
            # dp[i - 1] is money if you didnt buy anything that ends at i
            dp[i] = dp[i - 1]
            # compare different combinations of buys and previous buys
            for s, g in ints[i - 1]: 
                dp[i] = max(dp[i], dp[s] + g)
        
        return dp[n]
        
