class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        string = s.split(' ')

        #  pattern and string must be same "length"
        if len(string) != len(pattern): 
            return False

        # builds hashmap from pattern and string
        hashmap = {}
        for i in range(len(pattern)): 
            # if there is a repeated term in pattern, must be repeated in string
            if pattern[i] in hashmap: 
                if hashmap[pattern[i]] != string[i]: 
                    return False
            else: 
                hashmap[pattern[i]] = string[i]
        
        # checks if there are any duplicate values in hashmap
        if len(hashmap.values()) != len(set(hashmap.values())): 
            return False

        return True
