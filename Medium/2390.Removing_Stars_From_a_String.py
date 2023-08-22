class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # will hold solution
        stack = []

        for char in s: 
            if char == '*' and stack: # pop, but only if there is some chars
                stack.pop()
            elif char != '*': # just add char
                stack.append(char)
        
        # collapse list into string
        return ''.join(stack)
