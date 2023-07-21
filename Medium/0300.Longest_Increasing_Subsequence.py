class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # each term starts with a default sequence length of 1
        dp = [1] * len(nums)

        # iterate through nums and fill in dp array
        for i in range(1, len(nums)): 
            # go back in dp array to see if nums[i] builds on any previous sequences
            for j in range(i - 1, -1, -1): 
                # if nums[i] can build on any previous sequences
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # return the maximum sequence found
        return max(dp)
        
