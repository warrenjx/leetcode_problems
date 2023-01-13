class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = deque()

        for tok in s: 
            if tok == "(": 
                stack.append(1)
            elif tok == "[": 
                stack.append(2)
            elif tok == "{": 
                stack.append(3)
            elif not stack: 
                return False
            elif tok == ")": 
                if stack.pop() != 1: 
                    return False
            elif tok == "]": 
                if stack.pop() != 2: 
                    return False
            elif tok == "}": 
                if stack.pop() != 3: 
                    return False
            
        if not stack: 
            return True
        
        return False