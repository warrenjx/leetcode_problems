class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # edge case: only 1 term in array
        if len(nums) == 1: 
            return nums[0] == target

        # binary search
        hi = len(nums) - 1
        lo = 0

        while lo <= hi: 
            # get rid of duplicate terms at ends of range
            while lo < hi and nums[lo] == nums[lo + 1]: 
                lo += 1
            while lo < hi and nums[hi] == nums[hi - 1]: 
                hi -= 1
            
            # calculate midpoint and check
            mid = (hi + lo) // 2
            if nums[mid] == target: 
                return True

            # modified binary search conditions due to rotation
            if nums[lo] <= nums[mid]:
                if nums[mid] > target and nums[lo] <= target: # rotation not in here
                    hi = mid - 1
                else: # rotation possibly in here
                    lo = mid + 1
            else:
                if nums[mid] < target and target <= nums[hi]: # rotation not in here
                    lo = mid + 1
                else: # rotation possibly in here
                    hi = mid - 1
        
        return False
