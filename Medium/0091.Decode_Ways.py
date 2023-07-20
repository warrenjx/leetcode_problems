class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # edge case: leading zero at beginning
        if s[0] == "0": 
            return 0
        
        # ct_1 keeps track of sequences that end in a 1 digit letter
        #   starts at 1 because any nonzero digit is valid
        ct_1 = 1
        # ct_2 keeps track of sequences that end in a 2 digit letter
        ct_2 = 0

        # cache used to store the most recently parsed digit
        #   used to determine if there is a valid 2 digit letter combination
        cache = int(s[0])

        for i in range(1, len(s)): 
            curr = int(s[i])

            # current value of ct_1 is used to calculate ct_2
            old_ct_1 = ct_1

            if curr == 0: # if 0, it invalidates any sequences that end in 1 digit letter
                ct_1 = 0
            else: # else it continues all currently valid sequences, thus add ct_1 and ct_2
                ct_1 = ct_1 + ct_2

            if cache * 10 + curr <= 26: # if valid 2 digit letter, will continue off of every 1 digit letter sequence
                ct_2 = old_ct_1
            else: # if not valid, will invalidate all current 2 digit letter combinations
                ct_2 = 0

            # update cache
            cache = curr

        return ct_1 + ct_2
