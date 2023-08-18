class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # ct keeps track of the amount of edges connected to a node
        ct = [0] * n

        # increment ct at each end of each pair
        for pair in roads: 
            ct[pair[0]] += 1
            ct[pair[1]] += 1
        
        sol = -1
        # R is a set of roads for faster comparisons
        R = set([tuple(sorted(x)) for x in roads])

        # check each pair of cities for max rank
        for i in range(n): 
            for j in range(i + 1, n): 
                if (i, j) in R: # if they are connected, that node would be double counted
                    sol = max(sol, ct[i] + ct[j] - 1)
                else: # unconnected nodes, no need to minus
                    sol = max(sol, ct[i] + ct[j])

        return sol
