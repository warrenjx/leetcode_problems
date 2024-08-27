class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        # create adjacency list of nodes and edges
        adj_list = {}
        for i in range(n): 
            # format is: source: (destination, edge probability)
            adj_list[i] = []
        
        # add entries in adj list for both directions since it is undirected
        for i in range(len(edges)): 
            adj_list[edges[i][0]].append((edges[i][1], succProb[i]))
            adj_list[edges[i][1]].append((edges[i][0], succProb[i]))

        # probs keeps the highest probability to reach a specific node
        probs = [0] * n

        # queue for bfs/dijsktras
        q = deque()
        # start bfs at start node with maximum probability 1
        q.append((start_node, 1))

        # bfs from start node
        while q: 
            curr, prob = q.popleft()

            # only bfs from node if a new higher probability way is possible
            if (prob > probs[curr]): 
                probs[curr] = prob
            else: 
                continue
            
            # bfs to neighbors
            for dst, chance in adj_list[curr]: 
                q.append((dst, chance * prob))
        
        return probs[end_node]
