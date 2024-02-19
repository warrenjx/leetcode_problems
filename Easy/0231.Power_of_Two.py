class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # count number of bits in the number
        ct = 0
        while n >= 1: 
            if n & 1: 
                ct += 1

            n >>= 1
        
        # powers of 2 should only have 1 bit
        return ct == 1
