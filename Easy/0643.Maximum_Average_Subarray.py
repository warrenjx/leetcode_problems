class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # build initial prefix sum with sum of first k elements
        pref = sum(nums[:k])
        sol = pref

        # check the rest of the prefix sums
        for i in range(k, len(nums)): 
            # calculate next prefix sum
            pref += nums[i]
            pref -= nums[i - k]

            # check current prefix sum with max
            sol = max(sol, pref)

        return float(sol) / k
