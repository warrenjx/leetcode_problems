class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # start sol as firsts number in nums
        sol = nums[0]

        for i in range(1, len(nums)): 
            # xor numbers will cancel out duplicates
            sol ^= nums[i]

        return sol
