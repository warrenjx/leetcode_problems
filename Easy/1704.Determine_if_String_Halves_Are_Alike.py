class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # half the length of list
        offset = len(s) // 2
        # set for fast search
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        first = 0
        second = 0

        # count vowels in each half
        for i in range(offset): 
            if s[i] in vowels: 
                first += 1
            if s[i + offset] in vowels: 
                second += 1
        
        return first == second
        
