class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # sort by end rather than start to avoid n^2 method
        pairs.sort(key=lambda x:x[1])

        # the interval with the lowest end will be a part of solution
        end = pairs[0][1]
        sol = 1

        # check the rest of the pairs
        for i in range(1, len(pairs)): 
            if pairs[i][0] > end: # if an interval can be added to the chain
                end = pairs[i][1]
                sol += 1
        
        return sol
