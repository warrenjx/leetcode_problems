class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # basically calculate pascals triangle in place and modulo 10
        for i in range(len(nums) - 1): 
            for j in range(len(nums) - i - 1): 
                nums[j] = (nums[j] + nums[j + 1]) % 10
        
        return nums[0]
        
