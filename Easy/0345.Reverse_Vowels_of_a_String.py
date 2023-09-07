class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # set for quick lookups 
        V = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        # add all vowels to a stack
        vows = deque()
        for c in s: 
            if c in V: 
                vows.append(c)
        
        # replace vowels from stack in FIFO order (last first)
        sol = ""
        for c in s: 
            if c in V: 
                sol += vows.pop()
            else: 
                sol += c

        return sol
        
