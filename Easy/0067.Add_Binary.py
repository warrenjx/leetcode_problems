class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sol = ""

        # carry-in
        carry = 0

        # indeces for strings a and b
        i = len(a) - 1
        j = len(b) - 1 

        # add binary strings bit by bit
        while i >= 0 or j >= 0 or carry:
            # carry is the sum of all bits present 
            if i >= 0: 
                carry += int(a[i])
                i -= 1
            if j >= 0: 
                carry += int(b[j])
                j -= 1

            # 1 for 1 and 3
            sol = str(carry % 2) + sol

            # carry out is only when 2 or 3
            carry //= 2
        
        return sol
