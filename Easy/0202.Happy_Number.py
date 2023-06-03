class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # set for O(1) lookup times
        hashmap = set()

        while True: 
            if n in hashmap: # if it has been seen already (looping)
                return False
            elif n == 1: # is happy number
                return True
            
            hashmap.add(n)

            # calculate new number
            next_n = 0
            while n > 0: 
                next_n += (n % 10) ** 2
                n /= 10
            
            n = next_n
