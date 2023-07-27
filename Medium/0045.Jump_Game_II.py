class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [10001] * len(nums) # fill dp array with placeholder for now
        # first position reachable immediately
        dp[0] = 0

        # check how far you can jump from every position in nums
        for i in range(len(nums)): 
            # update dp with each jump distance
            for j in range(i + 1, min(len(nums), i + nums[i] + 1)): 
                # dp holds the minimum amount of jumps required to reach a certain point
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]
