class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # convenience variables
        n = len(s)
        m = len(t)

        # indices for iterating through s, t
        i = 0
        j = 0
        while i < n: 
            if s[i] == t[j]: # if characters match, move forward in both
                i += 1
                j += 1
            else: # else only move forward in s
                i += 1

            if j == m: # if t has been matched completely already
                return 0

        # no complete match, just return amount of remaining chars
        return m - j
