class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        ct = 1
        curr = nums[0]
        for i in range(1, len(nums)): 
            if ct > len(nums) // 2: 
                return curr
                
            if nums[i] == curr: 
                ct += 1
            else: 
                curr = nums[i]
                ct = 1

        return curr
