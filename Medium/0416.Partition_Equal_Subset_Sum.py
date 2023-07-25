class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # calculate the total sum of all the terms in nums
        total_sum = sum(nums)
        
        # if total sum is odd, then its impossible
        if total_sum % 2 == 1: 
            return False
        
        target = total_sum / 2
        
        # dp array holds booleans which dictate whether a certain value(index) is reachable
        dp = [False] * (target + 1)
        # 0 is reachable
        dp[0] = True

        # check each number and modify dp to show whats reachable after you add that number
        for num in nums: 
            # traverse backwards to avoid double counting numbers
            for i in range(target, num - 1, -1): 
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
