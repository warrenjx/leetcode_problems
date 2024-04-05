class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        # convert s to list so it can be changed
        s = list(s)
        n = len(s) - 1

        i = 0
        while i < n: 
            # if adjacent characters
            if (ord(s[i]) - 32 == ord(s[i + 1])) or (ord(s[i]) == ord(s[i + 1]) - 32): 
                # delete them
                del s[i]
                del s[i]

                n -= 2
                # so i doesnt go negative if adjacent characters are that the beginning
                i = max(0, i - 1)

                continue

            i += 1
        
        return ''.join(s)
