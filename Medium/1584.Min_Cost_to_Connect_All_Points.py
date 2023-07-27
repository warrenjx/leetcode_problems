class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)

        # create a list containing all possible edges in the graph
        edges = []
        for i in range(n): 
            for j in range(i + 1, n): 
                man_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                # format: (manhattan distance, start, end)
                # assign all points integer ids so its easier to union find with them
                edges.append((man_dist, i, j))
        
        # sort the list in order by manhattan distance
        edges.sort(key=lambda x:x[0])

        # initialize union data structure, each node is its own parent to start out
        union = [i for i in range(n)]

        # edge count used to tell when graph is fully connected
        edge_ct = 0

        sol = 0

        # general idea: add edges in order of least distance (Kruskal's Algorithm)
        #   check if start and end have different root nodes
        #   if same, discard edge, if different add edge
        for man, start, end in edges: 
            # if the 2 edges are already connected in the graph
            if self.root(union, start) == self.root(union, end): 
                continue
            
            # connect the 2 nodes
            self.build(union, start, end)
            # increment solution with manhattan distance and edge ct
            sol += man
            edge_ct += 1

            if edge_ct == n - 1: 
                break

        return sol
    
    # function joins 2 nodes in a union
    def build(self, union, start, end): 
        s_root = self.root(union, start)
        e_root = self.root(union, end)

        union[max(s_root, e_root)] = min(s_root, e_root)

    # function finds the root of node
    def root(self, union, node): 
        while union[node] != node: 
            node = union[node]
        
        return node
