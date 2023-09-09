class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # dop holds the amount of ways to reach number index with digits in nums
        dp = [0] * (target + 1)
        dp[0] = 1 # only 1 way to reach 0
        
        # since looking for ways to reach, not amount of difits needed, do number first
        for i in range(1, target + 1): 
            for num in nums: # options inside for ways to reach
                # dp[i] is the combination of all the ways to reach i with the current digits in nums
                if i - num >= 0:  
                    dp[i] += dp[i - num]

        return dp[-1]
