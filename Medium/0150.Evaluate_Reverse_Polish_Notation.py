class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        # deque() is faster than list if never have to use indeces
        stack = deque()

        for tok in tokens: 
            if tok == "+": 
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif tok == "-": 
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1) # order of operations
            elif tok == "*": 
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif tok == "/": 
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(float(n2) / n1)) # order of operations
            else: 
                stack.append(int(tok))
        
        return stack.pop()