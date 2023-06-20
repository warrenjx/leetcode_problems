class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sol = [-1] * len(nums)

        # calculate the rolling sum that will be used for the rest of the terms
        rolling_sum = 0
        for i in range(0, min(2 * k + 1, len(nums))): 
            rolling_sum += nums[i]
        
        # only enter it in the array if it can 
        if (2 * k) < len(nums): 
            sol[k] = rolling_sum // (2 * k + 1)

        # modify the rolling sum rather than recalculate each time
        for i in range(k + 1, len(nums) - k): 
            rolling_sum -= nums[i - k - 1]
            rolling_sum += nums[i + k]

            sol[i] = rolling_sum // (2 * k + 1)
        
        return sol
