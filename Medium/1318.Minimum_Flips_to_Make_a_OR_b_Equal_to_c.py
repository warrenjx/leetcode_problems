class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        sol = 0
        ab = a | b

        i = 1
        while i <= max(ab, c): # if not, the loop will end early if one is larger than the other
            if (i & c) and not (i & b) and not (i & a): # c is 1 but a and b are both 0
                sol += 1
            elif not (i & c) and (i & a) and not (i & b): # c is 0 and a is 1
                sol += 1
            elif not (i & c) and (i & b) and not (i & a): # c is 0 and b is 1
                sol += 1
            elif not (i & c) and (i & b) and (i & b): # c is 0 and a and b are both  1: 
                sol += 2

            i = i << 1

        return sol
