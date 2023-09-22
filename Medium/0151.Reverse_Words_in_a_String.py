class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # stack to holds words taken from the string
        stack = deque()

        # take words out from string
        tail = 0
        while s[tail] == ' ': 
            tail += 1
        for head in range(tail, len(s)): 
            if s[head] == ' ' and head >= tail: # if a complete word was found
                stack.append(s[tail:head])

                tail = head + 1
                while tail < len(s) and s[tail] == ' ': 
                    tail += 1
        
        # put words fifo out onto the string
        sol = None
        if s[-1] != ' ': 
            sol = s[tail:head + 1]
        else: 
            sol = stack.pop()
        while stack: 
            sol += " " + stack.pop()

        return sol
