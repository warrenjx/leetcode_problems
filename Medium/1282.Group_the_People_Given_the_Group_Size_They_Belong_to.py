class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        # holds mapping of group sizes to indeces who want it
        hashmap = {}
        sol = []

        # assign each index to its group
        for i in range(len(groupSizes)):
            # add index to group 
            if groupSizes[i] in hashmap:
                hashmap[groupSizes[i]].append(i)
            else: 
                hashmap[groupSizes[i]] = [i]
            
            # if amount of people who want that size group are in it, put it to sol
            if len(hashmap[groupSizes[i]]) == groupSizes[i]: 
                sol.append(hashmap[groupSizes[i]])
                hashmap[groupSizes[i]] = []
        
        return sol
        
