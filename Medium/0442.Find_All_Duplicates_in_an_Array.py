class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sol = []

        for i in range(len(nums)): 
            curr = abs(nums[i])

            # use the sign of the index to mark if index+1 has been seen before
            if nums[curr - 1] < 0: 
                sol.append(curr)
            else: 
                nums[curr - 1] = -nums[curr - 1]

        return sol
