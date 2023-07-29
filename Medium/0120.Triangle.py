class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        # each entry in dp represents the lowest cost way to get to it
        dp = []
        for i in range(n): 
            dp.append([-1] * len(triangle[i]))
        
        # initialize dp
        dp[0][0] = triangle[0][0]

        # populate the left and right edges of dp
        for i in range(1, n): 
            dp[i][0] = triangle[i][0] + dp[i - 1][0]
            dp[i][-1] = triangle[i][-1] + dp[i - 1][-1]

        # populate the interior of the dp triangle
        for i in range(2, n): 
            # populate each row individually
            for j in range(1, len(triangle[i]) - 1):
                # each entry is the min of its 2 possible paths + current cost 
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1])
    
