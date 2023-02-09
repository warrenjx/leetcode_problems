class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == "": 
            return true

        # use regex to get only characters
        s = "".join(re.findall("[a-zA-Z0-9]+", s)).lower()
        
        # check character against its opposite position in the string
        for i in range(len(s)): 
            if s[i] != s[len(s) - i - 1]: 
                return False
        
        return True