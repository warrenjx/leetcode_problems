class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # construct map of frequencies of characters
        chars = {}
        for c in s: 
            if c in chars: 
                chars[c] += 1
            else: 
                chars[c] = 1

        # if there is an odd frequency
        odd = False
        sol = 0

        for c, ct in chars.items(): 
            if ct % 2 == 0: # if even all chars can be used in palindrome
                sol += ct
            else: # if odd all but 1 can be used
                sol += ct - 1
                odd = True

        if odd: # one odd char will be the center char, thus +1
            return sol + 1
        else: 
            return sol
