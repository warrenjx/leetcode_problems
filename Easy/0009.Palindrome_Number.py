class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # all negatives aren't palindromes
        if x < 0: 
            return False
        
        # get the magnitude of the number
        mag = 1
        while mag * 10 <= x: 
            mag *= 10

        # check first and last digit iteratively
        while mag > 1: 
            if (x // mag) != (x % 10): 
                return False
            else: 
                # strip the most significant digit
                x -= (x // mag) * mag
                # strip the least significant digit
                x /= 10
                # decrement magnitude
                mag /= 100

        return True
