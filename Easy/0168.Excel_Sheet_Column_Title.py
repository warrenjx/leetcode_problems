class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        sol = ""

        while columnNumber > 0: 
            # calculate the next character
            curr = columnNumber % 26

            # edge case for the fact that its 1-based
            if curr == 0: 
                curr = 26
                columnNumber -= 26

            # fill in solution backwards
            sol = chr(64 + curr) + sol
            # decrement columnNumber
            columnNumber /= 26

        return sol
