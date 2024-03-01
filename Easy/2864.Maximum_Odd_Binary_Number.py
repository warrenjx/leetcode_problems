class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        # count number of 1s and zeros in the number
        ones = 0 
        zeros = 0
        for c in s:
            if c == '0': 
                zeros += 1
            else: 
                ones += 1
        
        # make bit 1, then the remaining bits at the MSB
        return "1" * (ones - 1) + "0" * zeros + "1"
