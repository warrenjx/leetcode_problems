class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ct = 0
        while n > 0: 
            # check if LSB is 1
            if n & 1: 
                ct += 1
            
            # get new LSB
            n >>= 1
        
        return ct
