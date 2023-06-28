class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # takes care of edge cases
        if len(nums) == 1: 
            return (nums[0] == target) - 1
        
        # idea: find how much it is rotated by and set the bounds accordingly
        rotated = 0

        # binary search to find the amount it has been rotated by
        hi = len(nums) - 1
        lo = 0
        while lo <= hi: 
            mid = (lo + hi) // 2

            # if do manage to find target here might as well return
            if nums[mid] == target: 
                return mid

            # sets rotated to index of minimum index
            if nums[mid] < nums[mid - 1]: 
                rotated = mid
                break
            elif nums[mid] > nums[mid + 1]: 
                rotated = mid + 1 
            
            # same method as find minimum in rotated sorted array
            if nums[mid] > nums[hi]: 
                lo = mid + 1
            else: 
                hi = mid - 1

        # set hi and lo based on rotated amount
        hi = 0
        lo = 0
        if rotated == 0: # no rotation means do binary search as normal
            hi = len(nums) - 1
            lo = 0
        elif target < nums[0]: # rotated, target is between min and max index
            hi = len(nums) - 1
            lo = rotated
        else: # rotated, target is between index 0 and min
            hi = rotated - 1
            lo = 0
        
        # regular binary search but with modified ranges for rotation
        while lo <= hi: 
            mid = (hi + lo) // 2
            
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target: 
                hi = mid - 1
            else: 
                lo = mid + 1

        return -1
