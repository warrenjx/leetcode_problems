class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        # dp holds whether or not 
        dp = [False] * (n + 1)

        dp[0] = True # seed starter position
        dp[2] = nums[0] == nums[1] # check first duo as loop needs to start at 3

        # main tabulation process
        for i in range(3, n + 1): 
            # each is separate if statement as they all need to be checked for every element
            if nums[i - 1] == nums[i - 2]: # case 1, 2 equal elements, propagate forward sol 2 elements ago
                dp[i] = dp[i] or dp[i - 2] # do or as the cases may overwrite each other
            if nums[i - 1] == nums[i - 2] == nums[i - 3]: # case 2: 3 equal elements, propagate sol 3 elements ago
                dp[i] = dp[i] or dp[i - 3]
            if nums[i - 1] - 2 == nums[i - 2] - 1 == nums[i - 3]: # case 3: 3 consecutive elements, same as above
                dp[i] = dp[i] or dp[i - 3]
        
        return dp[n]
