class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # edge cases: 
        if len(nums) <= 2: 
            return True

        # boolean to determine direction
        up = True
        # if the elements are all the same or not
        diff = True
        # holds the index where the real loop starts
        idx = 0
        for i in range(1, len(nums)): 
            if nums[i - 1] > nums[i]: 
                up = False
                diff = False
                idx = i
                break
            elif nums[i - 1] < nums[i]: 
                diff = False
                idx = i
                break

        # if all elements are identical, it is monotonic
        if diff: 
            return True
        
        # main checking loop
        for i in range(idx, len(nums)): 
            if up: 
                if nums[i] < nums[i - 1]: 
                    return False
            else: 
                if nums[i] > nums[i - 1]: 
                    return False

        return True
