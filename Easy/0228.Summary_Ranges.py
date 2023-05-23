class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # takes care of 0 and 1 edge cases
        if len(nums) == 0: 
            return []
        elif len(nums) == 1: 
            return [str(nums[0])]
        
        # main process which makes intervals for the array
        sol = []
        curr = 0

        for i in range(len(nums) - 1): 
            if nums[i + 1] != nums[i] + 1: 
                # new interval
                if i != curr: 
                    sol.append(str(nums[curr]) + "->" + str(nums[i]))
                else: 
                    sol.append(str(nums[curr]))
                curr = i + 1
        
        # makes intervals for last terms
        if len(nums) - 1 != curr: 
            sol.append(str(nums[curr]) + "->" + str(nums[len(nums) - 1]))
        else: 
            sol.append(str(nums[curr]))

        return sol
