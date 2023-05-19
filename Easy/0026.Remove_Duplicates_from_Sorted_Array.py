class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1

        curr_idx = 0; 

        for check_idx in range(1, len(nums)): 
            # if non duplicate, move it over an already checked or duplicated value
            if nums[check_idx] != nums[curr_idx]: 
                k += 1
                curr_idx += 1
                nums[curr_idx] = nums[check_idx]
        
        return k
