class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # initialize stack used for dfs 
        stack = deque()
        stack.append((0, [0]))

        sol = []
        # dfs the graph using adjacency list "graph"
        while stack: 
            curr, path = stack.pop()

            # visit node
            if curr == len(graph) - 1: 
                sol.append(path)

            # add to stack future nodes
            for num in graph[curr]: 
                stack.append((num, path + [num]))

        return sol
