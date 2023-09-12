class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        # edge case: only 1 long, no compression
        if n == 1: 
            return 1
        
        curr = chars[0] # represents the current character being compressed
        ct = 1 # how many of curr
        pos = 0 # pointer to where in the string will get rewritten

        # iterate through the string
        i = 1
        while i < n:
            if chars[i] == curr: # matching char, just increment count
                ct += 1
            else: # non-matching char, rewrite string
                chars[pos] = curr # put first char
                pos += 1 #
                # write number of char if more than one
                if ct > 1: 
                    order = 1
                    while order <= ct: # find order of magnitude of ct
                        order *= 10
                    order /= 10
                    while order > 0: # add digits of ct from most significant to least
                        chars[pos] = str(ct // order)
                        pos += 1
                        ct %= order
                        order /= 10
                
                # update curr and ct to current char
                curr = chars[i]
                ct = 1

            i += 1 
        
        # do the same as if nonmatch char for end of string
        chars[pos] = curr
        pos += 1
        if ct > 1: 
            order = 1
            while order <= ct: 
                order *= 10
            order /= 10
            while order > 0: 
                chars[pos] = str(ct // order)
                pos += 1
                ct %= order
                order /= 10
            
        return pos
