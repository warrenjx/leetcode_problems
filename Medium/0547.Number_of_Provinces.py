class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        visited = [False] * len(isConnected)

        stack = deque()
        stack.append(0)

        bfs_ct = 0
        
        # keep on BFS-ing until all nodes are visited
        while stack: 
            # run BFS on a node
            while stack: 
                curr = stack.popleft()

                visited[curr] = True

                for i in range(len(isConnected[curr])): 
                    if isConnected[curr][i] == 1 and visited[i] == False: 
                        stack.append(i)
            
            bfs_ct += 1

            # look for untouched nodes
            for i in range(len(visited)): 
                if visited[i] == False: 
                    stack.append(i)
                    break

        # amount of times BFS was run is amount of provinces
        return bfs_ct
