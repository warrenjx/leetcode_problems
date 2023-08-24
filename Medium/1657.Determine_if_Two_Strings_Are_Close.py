class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2): 
            return False
        
        # they will have the same lengths
        n = len(word1)

        # create a hashmap for each word, mapping characters to their occurances
        hash1 = {}
        hash2 = {}
        # fill in the hashmaps for word1 and word2
        for i in range(n): 
            if word1[i] in hash1: 
                hash1[word1[i]] += 1
            else: 
                hash1[word1[i]] = 1
            
            if word2[i] in hash2: 
                hash2[word2[i]] += 1
            else: 
                hash2[word2[i]] = 1

        # W# is a set of all the characters in each word
        W1 = hash1.keys()
        W2 = hash2.keys()
        # sort the sets
        W1.sort()
        W2.sort()

        # C# is the sets of all the occurances of characters in each word
        C1 = hash1.values()
        C2 = hash2.values()
        # sort the sets
        C1.sort()
        C2.sort()

        # if the sets are equal, the swap can be made
        if W1 == W2 and C1 == C2: 
            return True
        else: 
            return False
