class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # simple binary search
        left = 0
        right = len(nums) - 1

        while left <= right: 
            place = (left + right) // 2

            if (nums[place] < target): 
                left = place + 1
            elif (nums[place] > target): 
                right = place - 1
            else: 
                return place
        
        #except if not found return place it could have been
        return left