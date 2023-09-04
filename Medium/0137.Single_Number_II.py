class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # bits holds the number of bits at the i'th place in binary digit
        bits = [0] * 32
        # count the number of bits in each place over all numbers
        for num in nums: 
            for i in range(32): 
                if num & (1 << i): 
                    bits[i] += 1
        
        # convert it back into a singular digit
        sol = 0
        for i in range(31, -1, -1): 
            sol *= 2 # move current sol
            sol += bits[i] % 3 # if %3 > 0 then there must be a non tri-duplicated digit

        # adjusting back to negative numbers since python int isnt bound
        if sol > 2147483647: 
            # 2's complement conversion
            sol -= 4294967295 + 1

        return sol
