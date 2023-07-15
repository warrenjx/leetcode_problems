class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize dp array, need first 3 terms to start
        dp = nums[0:3]

        # edge cases for size 1 and 2 where algo doesn't work
        if len(nums) == 1: 
            return dp[0]
        elif len(nums) == 2: 
            return max(dp)

        dp[2] += dp[0]
        
        for i in range(3, len(nums)): 
            # sub problem is the max of the past 3 terms minus term just before current
            dp.append(max(dp[i - 2], dp[i - 3]) + nums[i])

        return max(dp[-1], dp[-2])
