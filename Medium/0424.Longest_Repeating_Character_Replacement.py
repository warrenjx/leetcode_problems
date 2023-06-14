class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_len = 0 
        # use list to store counts of all letters
        counts = [0] * 26

        curr = None

        tail = 0
        for i in range(len(s)): 
            letter = ord(s[i]) - ord('A')
            counts[letter] += 1
            
            # current count is the window size
            curr_ct = i - tail + 1
            # if there is a character in the window which has atleast curr_ct - k occurances
            if curr_ct - max(counts) <= k: 
                max_len = max(max_len, curr_ct)
            else: 
                # else increment the tail and decrement the character at the former tail
                counts[ord(s[tail]) - ord('A')] -= 1
                tail += 1
        
        return max_len
