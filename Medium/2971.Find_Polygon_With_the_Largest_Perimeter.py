class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort the numbers for easier greedy approach
        nums.sort()

        # prefix sum is initially if the shape involves all sides
        prefix_sum = sum(nums)
        
        # stop at 2 because polygon needs at least 3 edges
        for i in range(len(nums) - 1, 1, -1): 
            # condition for valid polygon: sides are connected
            if prefix_sum > (nums[i] * 2): # longest side must be less than sum of all other sides
                return prefix_sum
            
            # decrement prefix sum if edge could not be included
            prefix_sum -= nums[i]
        
        # if no valid polygons were found
        return -1
