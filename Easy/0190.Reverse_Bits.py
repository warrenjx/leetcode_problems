class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sol = 0

        # do it for 32 rounds because it is 32 bits
        for _ in range(32): 
            # shift left regardless
            sol <<= 1
            # or in a 1 if there is a 1
            if n & 1 == 1: 
                sol |= 1
            
            # decrement n
            n >>= 1

        return sol
