class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # lengths of the 2 strings for ease of use
        n = len(s1)
        m = len(s2)

        # if s2 is shorter than s2 then impossible
        if m < n: 
            return False
        
        # lists for keeping track of the amount of characters in each substring
        ct_1 = [0] * 26
        ct_2 = [0] * 26

        # populate the substring for s1
        for char in s1: 
            ct_1[ord(char) - ord('a')] += 1
        
        # populate the beginning of the substring for s2
        for i in range(0, n): 
            ct_2[ord(s2[i]) - ord('a')] += 1

        # sliding window process
        for i in range(n, m + 1):
            # compare the 2 character counts 
            if ct_1 == ct_2: 
                return True

            # loop runs one more time so it checks for the last time
            if i == m: 
                break

            # update character count for moving foward
            ct_2[ord(s2[i]) - ord('a')] += 1
            # decrement character count for character being left
            ct_2[ord(s2[i - n]) - ord('a')] -= 1

        return False
