class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # hashmap holds mapping of characters to their frequencies
        char_map = {}
        # populate hashmap
        for c in s: 
            if c in char_map: 
                char_map[c] += 1
            else: 
                char_map[c] = 1

        # turn hashmap into key value pairs so it can be sorted
        char_map = char_map.items()
        # sort it in order of its frequencies, largest to smallest
        char_map.sort(key=lambda x: x[1], reverse=True)

        # add the characters and their corresponding frequencies to sol
        sol = ""
        for char, cts in char_map: 
            sol += char * cts
        
        return sol
