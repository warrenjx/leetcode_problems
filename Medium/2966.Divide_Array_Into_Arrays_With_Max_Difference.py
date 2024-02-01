class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # edge case less than 3 no solution
        if len(nums) < 3: 
            return None

        # sorting makes this trivial
        nums.sort()

        sol = []

        idx = 0
        # add groups of 3 if they are all within k
        while idx < len(nums): 
            start = nums[idx]
            row = [start]

            for i in range(1, 3): 
                if nums[idx + i] <= start + k: 
                    row.append(nums[idx + i])
                else: 
                    return None
            
            sol.append(row)
            idx += 3

        return sol
