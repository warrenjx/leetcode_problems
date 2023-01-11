class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1: 
            return len(nums)

        # gets rid of duplicates and sorts
        nums = list(set(nums))
        nums.sort()

        sol = 0
        temp = 0

        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1] + 1: 
                temp += 1
            else: 
                if temp > sol: 
                    sol = temp
                temp = 0
        
        return max(sol, temp) + 1 # max because else won't trigger if array ends