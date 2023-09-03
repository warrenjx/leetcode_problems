class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case: only 1 item in nums, messes with checking logic
        if len(nums) == 1: 
            return 0

        # variables for binary search
        hi = len(nums) - 1
        lo = 0
        # binary search works because can return any peak
        while lo <= hi: 
            mid = (hi + lo) // 2

            if mid == 0 and nums[mid] > nums[mid + 1]: # if at beginning of nums
                return mid
            elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]: # if at end of nums
                return mid
            elif nums[mid - 1] < nums[mid] > nums[mid + 1]: # check if greater than both neighbors
                return mid
            
            if nums[mid] < nums[mid + 1]: # if on the left slope of a peak
                lo = mid + 1
            else: # must be on right slope of a peak
                hi = mid - 1

        return lo
        
