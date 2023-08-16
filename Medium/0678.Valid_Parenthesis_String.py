class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_p = 0 # keeps track of minimum amount of unfulfulled parentheses
        max_p = 0 # keeps track of maximum amount of unfulfilled parentheses

        # iterate through string and update min and max p
        for char in s: 
            if   char == '(': # open parentheses increases both min and max
                min_p += 1
                max_p += 1
            elif char == ')': 
                min_p = max(0, min_p - 1) # min cannot drop below 0
                max_p -= 1 # max can, as it will be checked later
            elif char == '*': 
                min_p = max(0, min_p - 1) # for * treat min same as closing
                max_p += 1 # for max treat same as opening
            
            if max_p < 0: # since min cannot drop below 0, if max does its False
                return False
        
        # if minimum is 0, it is possible
        return min_p == 0
