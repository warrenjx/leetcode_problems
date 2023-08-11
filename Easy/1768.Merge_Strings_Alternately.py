class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # convenience variables
        n = len(word1)
        m = len(word2)

        # build sol up iteratively
        sol = ""

        # add them alterating
        for i in range(min(n, m)): 
            sol += word1[i]
            sol += word2[i]

        # add remaining if one is longer than the other
        if n < m: 
            sol += word2[n:]
        elif m < n: 
            sol += word1[m:]
        
        return sol
