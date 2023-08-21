class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_sum = 0 # left sum starts at 0
        r_sum = sum(nums[1:]) # right sum starts at all terms except for nums[0]

        # check every term in loop besides last
        for i in range(len(nums) - 1): 
            if l_sum == r_sum: # check sums
                return i
            
            l_sum += nums[i] # increment left sum
            r_sum -= nums[i + 1] # decrement right sum
        
        # check the last term
        if l_sum == r_sum: 
            return len(nums) - 1

        # no pivot found
        return -1
