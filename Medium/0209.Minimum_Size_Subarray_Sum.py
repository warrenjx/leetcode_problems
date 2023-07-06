class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # default value to make sure it gets set if a lower is found
        sol = len(nums)
        found = False

        # sm is the prefix sum of the array
        sm = 0
        # the tail end of the sliding window
        end = 0
        
        for i in range(len(nums)):  
            sm += nums[i]
            
            # shrink the sliding window until it is too small
            while sm >= target: 
                found = True

                # every time sliding window shrinks, check if it is greater than target
                sol = min(sol, i - end + 1)

                # shrink the sliding window
                sm -= nums[end]
                end += 1
        
        if found: 
            return sol
        else: 
            return 0
