class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sol = 0

        for i in range(len(nums) - 2, -1, -1): 
            if nums[i] > nums[i + 1]: 
                # calculate the amount of times it needs to be divided to become less than or equal to num above
                k = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

                sol += k - 1 # add operations to solution
                nums[i] = nums[i] // k # set nums[i] to the smallest term it ended up being split into
        
        return sol
