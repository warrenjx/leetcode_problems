class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # hashmap stores the first occurance index in string
        hashmap = {}
        for i in range(len(s)): 
            if s[i] in hashmap: # if it is repeated, set it to -1
                hashmap[s[i]] = -1
            else:
                hashmap[s[i]] = i
        
        # go through hashmap to find minimum
        sol = 100001
        for idx in hashmap.values(): 
            if idx != -1: 
                sol = min(sol, idx)

        if sol != 100001: # if it is a dupe sol would not have changed
            return sol
        else: 
            return -1
        
