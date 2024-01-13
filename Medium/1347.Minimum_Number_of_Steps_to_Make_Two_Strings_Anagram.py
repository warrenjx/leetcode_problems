class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_ct = {}
        t_ct = {}

        # create hashtable keeping track of how many of each character there is in each string
        for i in range(len(s)): 
            if s[i] in s_ct: 
                s_ct[s[i]] += 1
            else: 
                s_ct[s[i]] = 1
            if t[i] in t_ct: 
                t_ct[t[i]] += 1
            else: 
                t_ct[t[i]] = 1

        # count how many matching characters there are 
        matched = 0
        for key, freq in s_ct.items(): 
            if key in t_ct: 
                matched += min(freq, t_ct[key])

        # the difference between length and matched are how many characters need to be changed
        return len(s) - matched
        
