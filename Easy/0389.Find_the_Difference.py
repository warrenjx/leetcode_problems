class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # sort for easy comparisons
        s = sorted(s)
        t = sorted(t)

        # check which one has the letter added into it
        s_greater = False
        if len(s) > len(t): 
            s_greater = True

        # check each char
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]: 
                if s_greater: 
                    return s[i]
                else: 
                    return t[i]
        
        # different char is at the end
        if s_greater: 
            return s[-1]
        else: 
            return t[-1]
