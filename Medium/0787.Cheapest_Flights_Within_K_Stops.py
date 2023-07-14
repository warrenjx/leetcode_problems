class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # build adjacency list and price map from input flights
        # format: source : [(destination, link price)]
        adj_list = [[] for i in range(n)]
        for source, dest, price in flights: 
            adj_list[source].append((dest, price))
            
        # create array of minimum costs to reach each node
        min_prices = [999999 for i in range(n)] # 999999 is a placeholder number

        # bfs the graph
        queue = deque()
        # format: (curr node, curr price)
        queue.append((src, 0))

        # bfs only k levels deep
        stops = 0
        
        while queue and stops <= k: 
            width = len(queue)
            for i in range(width): 
                curr, price = queue.popleft()

                if not adj_list[curr]: 
                    continue 

                # visit neighbors
                for neighbor, cost in adj_list[curr]: 
                    # reduces runtime by skipping inefficient routes
                    if price + cost >= min_prices[neighbor]: 
                        continue
                    
                    min_prices[neighbor] = price + cost
                    queue.append((neighbor, price + cost))
            
            stops += 1

        if min_prices[dst] == 999999: # if still placeholder, was not able to reach it
            return -1
        else: 
            return min_prices[dst]
