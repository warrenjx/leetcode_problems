class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        stack = deque()
        sol = []

        stack.append(("(", 1))
        while stack: 
            curr, bal = stack.pop()

            if bal < 0: # invalid case
                continue
            elif (len(curr) == (n * 2)): # completed case 
                if bal == 0:  
                    sol.append(curr)
            else: # unfinished case
                stack.append((curr + "(", bal + 1))
                stack.append((curr + ")", bal - 1))    
        
        return sol