class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for ast in asteroids: 
            if ast < 0: 
                # if the most recent is negative or it is first term, won't be hit by anything
                if not stack or stack[-1] < 0: 
                    stack.append(ast)
                    continue
                
                # decide what to do with negative asteroid
                equal = False
                while stack: 
                    if stack[-1] < 0: # add to stack if a surviving negative asteroid
                        stack.append(ast)
                        break
                    elif stack[-1] > abs(ast): # most recent asteroid is greater, current breaks
                        break
                    elif stack[-1] == abs(ast): # they are equal, both break
                        equal = True
                        stack.pop()
                        break
                    else: # this asteroid is greater, new ast breaks most recent
                        stack.pop()
                
                # if a negative asteroid breaks all the asteroids in the stack currently
                if not stack and not equal: 
                    stack.append(ast)
            else: 
                # add all positive asteroids 
                stack.append(ast)
                    
        return stack
