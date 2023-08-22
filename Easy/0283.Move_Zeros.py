class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # count to hold the amount of nonzero chars seen
        ct = 0

        # shift nonzero characters forward
        for i in range(len(nums)): 
            if nums[i] != 0: 
                nums[ct] = nums[i]
                ct += 1
        
        # fill end of nums with zero
        for i in range(ct, len(nums)): 
            nums[i] = 0
        
        # no return because in place
        return
