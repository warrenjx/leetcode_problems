class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1: 
            return nums[0]
        
        max_ct = 0

        # count 1s and if not 1 restart count
        # keep track of max seen
        ct = 0
        for num in nums: 
            if num == 1: 
                ct += 1
            if num == 0: 
                max_ct = max(max_ct, ct)
                ct = 0
        
        # incase last term is 1, recalculate max_ct
        return max(max_ct, ct)
