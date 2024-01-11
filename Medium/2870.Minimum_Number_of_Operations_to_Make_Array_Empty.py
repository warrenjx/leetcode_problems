class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # create dictionary mapping number ot how often it appears in array
        counts = {}
        for num in nums: 
            if num in counts: 
                counts[num] += 1
            else: 
                counts[num] = 1
        
        sol = 0

        # check each number to see if it can be removed
        for num, freq in counts.items(): 
            if (freq == 1): # it 1, automatic failure
                return -1
            else: # other numbers can be removed
                if (freq % 3 == 0): # use only 3s
                    sol += freq // 3
                elif ((freq - 1) % 3 == 0): # have to replace 1 3 with 2 2s
                    sol += freq // 3 + 1
                elif ((freq - 2) % 3 == 0): # have to replace a 3 with a 2
                    sol += freq // 3 + 1 

        return sol
        
