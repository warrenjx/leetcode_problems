class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        if source == destination: 
            return True
        if not edges: 
            return False

        # create the baseline union data structure
        union = [0] * n
        for i in range(1, n): 
            union[i] = i

        # build union recursively
        for edge in edges: 
            l, r = edge
            self.union_build(union, l, r)

        # check if the source and destinations have the same root
        return self.root(union, source) == self.root(union, destination)
    
    # if they are connected edges, set their roots equal to each other
    def union_build(self, union, l, r): 
        union[self.root(union, l)] = self.root(union, r)
    
    # find the roots of 2 different nodes
    def root(self, union, node): 
        while (union[node] != node): 
            union[node] = union[union[node]]
            node = union[node]
        
        return node
