class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # edge cases of only 1 char and if different length strings
        if len(goal) == 1: 
            return False
        elif len(goal) != len(s): 
            return False

        # builds hashtable mapping characters to their indices
        hashtable = {}
        for i in range(len(goal)):
            if goal[i] in hashtable: 
                hashtable[goal[i]].add(i)
            else:  
                hashtable[goal[i]] = {i}
        
        # swap keeps track of character mismatches
        swap = []
        for i in range(len(s)): 
            if s[i] not in hashtable: 
                return False
            elif i not in hashtable[s[i]]: 
                swap.append((i, s[i]))
        
        # if 2 characters are swapped
        if len(swap) == 2 and swap[0][0] in hashtable[swap[1][1]] and swap[1][0] in hashtable[swap[0][1]]: 
                return True

        # case for duplicate characters
        if s == goal and len(s) > len(hashtable): 
            return True

        return False
