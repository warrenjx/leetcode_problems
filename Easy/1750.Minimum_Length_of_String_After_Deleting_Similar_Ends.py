class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        # tokens holds all of the same character sections 
        tokens = []
        # populate tokens
        prev = s[0]
        for i in range(1, len(s)): 
            if s[i] != prev[0]: 
                tokens.append(prev)
                prev = s[i]
            else: 
                prev += s[i]

        tokens.append(prev)

        # remove like prefix/postfixes of tokens
        l = 0
        r = len(tokens) - 1
        while l < r: 
            if tokens[l][0] == tokens[r][0]: # if equal then remove them
                l += 1
                r -= 1
            else: # not equal then can no longer remove
                break

        # solution of 0 is base case
        sol = 0
        if l == r: # if only 1 token remains at it is 1 length, else sol of 0 is possible
            if len(tokens[l]) == 1: 
                sol = 1
        else: # if multiple tokens remain, just take the rest
            for i in range(l, r + 1): 
                sol += len(tokens[i])

        return sol
