class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maintain the current sum of all elements so far
        pref_sum = nums[0]

        # minimum of all the sums so far
        min_sum = min(0, pref_sum)

        sol = pref_sum

        for i in range(1, len(nums)): 
            pref_sum += nums[i]
            
            # the max sum is the maximum minus the minimum sum so far
            sol = max(sol, pref_sum - min_sum)
            
            min_sum = min(min_sum, pref_sum)

        return sol
