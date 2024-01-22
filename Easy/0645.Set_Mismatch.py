class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # convenience variable
        n = len(nums)

        # calculate the difference between the repeated and missing elements
        ideal_sum = n * (n + 1) / 2
        real_sum = sum(nums)

        offset = abs(ideal_sum - real_sum)

        # intialize "bit vector"
        vector = [0] * n
        double = -1

        # go through terms and increment array
        for i in range(n): 
            if vector[nums[i] - 1] == 1: 
                double = nums[i]
            else: 
                vector[nums[i] - 1] = 1

        sol = [-1] * 2
        
        # first term is the repeated term
        sol[0] = double

        if double - 1 >= offset and double - 1 + offset < n: # if it could be either way
            if vector[double - 1 - offset] == 0: 
                sol[1] = double - offset
            else: 
                sol[1] = double + offset
        elif double - 1 >= offset: # just below
            if vector[double - 1 - offset] == 0: 
                sol[1] = double - offset
        elif double - 1 + offset < n: # just above
            if vector[double - 1 + offset] == 0:
                sol[1] = double + offset

        return sol
