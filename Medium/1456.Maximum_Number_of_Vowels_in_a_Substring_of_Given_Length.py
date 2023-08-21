class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # use a set for faster comparisons
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # find the vowel count of the initial k chars of s
        v_ct = 0
        for i in range(k): 
            if s[i] in vowels: 
                v_ct += 1

        sol = v_ct

        # check the remaining subarrays
        for i in range(k, len(s)): 
            # if new character is vowel, increment count
            if s[i] in vowels: 
                v_ct += 1
            # if previous character was a vowel, decrement count
            if s[i - k] in vowels: 
                v_ct -= 1
            
            sol = max(sol, v_ct)

        return sol
