class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # initialize union data structure
        union = len(edges) * [0]
        for i in range(1, len(edges)): 
            union[i] = i
        
        sol = []

        # build union iteratively
        for edge in edges: 
            l, r = edge
            # if 2 ends of an edge share a root, it is a redundant edge
            if self.root(union, l - 1) == self.root(union, r - 1): 
                sol.append([l, r])
            else: 
                self.build_union(union, l - 1, r - 1)

        print(union)

        return sol[-1]

    # function assigns 2 nodes to the same union by setting them to their roots
    def build_union(self, union, l, r): 
        union[self.root(union, l)] = self.root(union, r)
    
    # finds the root by tracing indeces until it reaches it
    def root(self, union, node): 
        while(union[node] != node): 
            union[node] = union[union[node]]
            node = union[node]
        
        return node