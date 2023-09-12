class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # counts maps characters to their frequencies in s
        counts = {}
        for c in s: 
            if c in counts: 
                counts[c] += 1
            else: 
                counts[c] = 1

        # freqs maps frequencies to how many characters share a frequency
        freqs = {}
        for char, ct in counts.items(): 
            if ct in freqs: 
                freqs[ct] += 1
            else: 
                freqs[ct] = 1

        n = max(freqs.keys())

        # occur[i] is how many chars appear i times in s
        occur = [0] * (n + 1)
        for fr, ct in freqs.items(): 
            occur[fr] = ct

        sol = 0
        for i in range(n, 0, -1): 
            if occur[i] > 1: # if a frequency is repeated
                ops = occur[i] - 1 # find out how many operations to make it alone (remove 1 of each char)
                occur[i] = 1
        
                # increment solution and next smallest frequency
                sol += ops
                occur[i - 1] += ops
                
        return sol
