class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # hashmap will map numbers to their occurances
        hashmap = {}
        # populate hashmap
        for num in arr:
            if num in hashmap: 
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        # occurances is a set containing each unique occurance count
        occurances = set()
        # check occurances against set
        for occur in hashmap.values(): 
            if occur in occurances: # if a duplicate is found
                return False
            else: 
                occurances.add(occur)

        return True
