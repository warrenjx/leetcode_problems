class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # dp holds the calculated subproblems
        #   the greatest sum will be in the rightmost column of the row
        dp = [[0] * n for i in range(n)]

        # fill in dp backwards
        for i in range(n - 1, -1, -1):
            # gradually expand subproblem range as you move up 
            for j in range(i, n): 
                # calculate every single possibility for each subproblem
                for k in range(i, j + 1): 
                    # variables which hold the left and right sums of the array after you pop nums[k]
                    left = 0
                    right = 0
                    # left and right sums are already calculated as they are subproblems
                    if k > i: 
                        left = dp[i][k - 1]
                    if k < j: 
                        right = dp[k + 1][j]

                    mid = nums[k]
                    # calculate the score if you popped nums[k] 
                    if i - 1 >= 0: 
                        mid *= nums[i - 1]
                    if j + 1 < n: 
                        mid *= nums[j + 1]

                    # check current score against the current best of the tile
                    dp[i][j] = max(dp[i][j], left + right + mid)

        # best of each row is stored in rightmost column
        return dp[0][-1]
