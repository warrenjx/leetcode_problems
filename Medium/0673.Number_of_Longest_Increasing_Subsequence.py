class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # format: [[length of longest subsequence, frequency]]
        dp = [[1, 1] for i in range(len(nums))]

        # very similar general process to number of longest increasing subsequence
        for i in range(1, len(nums)): 
            for j in range(i - 1, -1, -1): 
                # if nums[i] builds on an existing subsequence
                if nums[i] > nums[j]: 
                    # if a new longest sequence was formed for nums[i]
                    if dp[i][0] <= dp[j][0]: 
                        dp[i][0] = dp[j][0] + 1

                        # also increase its frequency to the one its building on
                        dp[i][1] = dp[j][1]
                        # continue so it doesn't get double incremented
                        continue

                    # if it is building on one 
                    if dp[i][0] - 1 == dp[j][0]: 
                        dp[i][1] += dp[j][1]
        
        # sum up all the frequencies of the longest increasing subsequences
        top = max(dp)[0]
        sol = 0

        for i in range(len(nums)): 
            if dp[i][0] == top: 
                sol += dp[i][1]
        
        return sol
