class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # memoization array for past calculations
        memo = {}

        # convenience variable
        n = len(nums)
        # same amount of operations to reach positive or negative version of target
        target = abs(target)

        # recursive dfs
        def dfs(curr, pos): 
            # base case for recursion
            if pos == n: 
                if curr == target: # target found
                    return 1
                else: # target is not found
                    return 0
            
            if (curr, pos) in memo: # calculation has been completed already, return cached answer
                return memo[(curr, pos)]
            else: # calculation is new, dfs it
                memo[(curr, pos)] = dfs(curr + nums[pos], pos + 1) + dfs(curr - nums[pos], pos + 1)

                return memo[(curr, pos)]
        
        return dfs(0, 0)
        
