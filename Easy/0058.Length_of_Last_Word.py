class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # separate words into list
        s = s.split(' ')
        
        # find last entity not empty
        idx = 1
        while s[-idx] == "": 
            idx += 1
        
        return len(s[-idx])
