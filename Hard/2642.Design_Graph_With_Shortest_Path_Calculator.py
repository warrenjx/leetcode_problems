class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        # add node count
        self.node_ct = n

        # initialize adjacency list with no edges from each node
        self.adj_list = [[] for i in range(n)]

        # add all the initial edges
        for src, dst, cost in edges: 
            self.adj_list[src].append((dst, cost))

        

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        # add edge to adjacency list
        self.adj_list[edge[0]].append((edge[1], edge[2]))


    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        # intialize node distances as arbitrarily high
        dists = [999999999] * self.node_ct
        # set cost of start node
        dists[node1] = 0

        # heap format: (cost at node, current node)
        heap = [(0, node1)] 

        # run dijstra's from node1 to node2
        while heap: 
            cost, curr = heappop(heap)

            # if target node found
            if curr == node2: 
                return cost

            # explore neighbors
            for dst, weight in self.adj_list[curr]: 
                new_cost = cost + weight

                # only explore neighbors if a new lower cost is possible (protects against cycles)
                if dists[dst] > new_cost: 
                    dists[dst] = new_cost
                    heappush(heap, (new_cost, dst))

        # if no path was found
        if dists[node2] == 999999999:
            return -1
        else:
            return dists[node2]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
