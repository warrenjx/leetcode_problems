class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # create hashmap of the characters in the pattern
        p_hash = {}
        for char in p: 
            if char in p_hash: 
                p_hash[char] += 1
            else: 
                p_hash[char] = 1

        # if pattern is longer than string, cannot be solved
        if len(p) > len(s): 
            return None

        # create hashmap of characters in the first len(p) - 1 characters of the string
        s_hash = {}
        for i in range(len(p) - 1): 
            if s[i] in s_hash: 
                s_hash[s[i]] += 1
            else: 
                s_hash[s[i]] = 1
        
        sol = []
        # iterate through the string, maintain sliding window of length len(p) to check against p
        for i in range(len(p) - 1, len(s)):
            # add new character 
            if s[i] in s_hash: 
                s_hash[s[i]] += 1
            else: 
                s_hash[s[i]] = 1

            # check character content against pattern
            if s_hash == p_hash: 
                sol.append(i - (len(p) - 1))
            
            # remove old character
            s_hash[s[i - (len(p) - 1)]] -= 1
            if s_hash[s[i - (len(p) - 1)]] == 0: 
                del s_hash[s[i - (len(p) - 1)]]
        
        return sol
        
