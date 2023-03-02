class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # use a hash table to store seen characters
        seen_chars = {}
        curr_max = 0

        tail = 0
        for head in range(len(s)): 
            # updates rear of substring only if it is a duplicate character
            if s[head] in seen_chars: 
                tail = max(tail, seen_chars[s[head]] + 1)
            
            # adds/updates character in hash table
            seen_chars[s[head]] = head

            # checks if new maximum was found
            curr_max = max(curr_max, head - tail + 1)

        return curr_max
