class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l1 = [1] * len(nums)
        l2 = [1] * len(nums)

        # l1 is product of terms offset from index 0
        # l2 is product of terms offset from index -1
        for i in range(1, len(nums)): 
            l1[i] = nums[i - 1] * l1[i - 1]
            l2[-i - 1] = nums[-i] * l2[-i]
        
        sol = [1] * len(nums)

        # multiplying the offset products gives the desired result
        # offset ends up omitting the current term
        for i in range(len(nums)): 
            sol[i] = l1[i] * l2[i]
        
        return sol
