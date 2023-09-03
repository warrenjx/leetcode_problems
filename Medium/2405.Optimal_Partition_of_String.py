class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = 0
        # hashmap stores seen characters in this partition
        hashmap = set()

        # iterate through string char by char
        for char in s: 
            if char in hashmap: # if the char is already in the partition
                sol += 1 # increment partition count
                hashmap = set(char) # create a new partition on this char
            else: # if char is new jsut add it
                hashmap.add(char)
        
        return sol + 1
        
