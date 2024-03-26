class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # reformat all terms outside of reasonable range
        for i in range(n): 
            if nums[i] <= 0:
                nums[i] = n + 1
            elif nums[i] > n: 
                nums[i] = n + 1
        
        # check if numbers 1 - n are present by using them as indeces and nums as the storage
        for i in range(n): 
            curr = abs(nums[i])

            if curr > n: # term was invalid
                continue
            elif nums[curr - 1] > 0: # term is present
                nums[curr - 1] = -nums[curr - 1]

        for i in range(n): # look for the first non-present index
            if nums[i] > 0: 
                return i + 1

        # all numbers 1 - n were present, thus n + 1 is lowest possible integer
        return n + 1
