class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = 0
        
        # since it is guaranteed to be correct, don't have to use a stack
        depth = 0
        for c in s: 
            if c == '(': # opening parentheses
                depth += 1
                sol = max(sol, depth)
            elif c == ')': # closing parentheses
                depth -= 1
            
        return sol
