class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case where algorithm ends up being out of range
        if len(nums) == 1: 
            return nums[0]

        hi = len(nums) - 1
        lo = 0

        while hi >= lo: 
            mid = (hi + lo) / 2

            # checking if min is near enough mid to test for it
            if nums[mid + 1] < nums[mid]: # if mid is the max and min is right after mid
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]: # if mid is the min and before it is the max
                return nums[mid] 

            # deciding which half to search
            if nums[hi] > nums[mid]: # hi half is in order, min cant be there
                hi = mid - 1
            else: # hi half is not in order, must be here
                lo = mid + 1

        return nums[lo]
