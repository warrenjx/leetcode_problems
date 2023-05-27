class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # create hashmap
        dic = {}
        for i in range(len(s)): 
            if s[i] in dic: 
                if dic[s[i]] != t[i]: 
                    return False
            else: 
                dic[s[i]] = t[i]
        
        # make sure there are no duplicate keys
        if len(dic.values()) != len(set(dic.values())): 
            return False
        
        return True
