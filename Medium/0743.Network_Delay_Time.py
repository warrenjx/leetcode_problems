class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # create adjacency list and network time map
        adj_list = {}
        # format: source : [(destination, link time)]
        for src, dst, time in times: 
            if src in adj_list: 
                adj_list[src].append((dst, time))
            else: 
                adj_list[src] = [(dst, time)]

        # initialize array denoting min time it takes to reach a node from k
        min_times = [1000000] * n # placeholder big number
        # initialize min time for starting point
        min_times[k - 1] = 0

        # bfs the grid
        queue = deque()
        # format: (node, time to reach node from k)
        queue.append((k, 0))

        while queue: 
            curr, time = queue.popleft()

            if curr not in adj_list: 
                continue
            
            # visit neighbors
            for neighbor, duration in adj_list[curr]: 
                # value of min_times[x] is the fastest time to reach it from k
                if duration + time < min_times[neighbor - 1]: 
                    min_times[neighbor - 1] = duration + time
                    queue.append((neighbor, duration + time))
        
        # if any times still placeholder, graph is not connected
        for i in min_times: 
            if i == 1000000: 
                return -1
        
        # slowest node is time for entire graph
        return max(min_times)
