class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # create a set representing terminal nodes/nodes that go to terminal nodes
        terms = set()
        # add all initial terminal nodes
        for i in range(len(graph)):  
            if not graph[i]: 
                terms.add(i)
        
        # explored will help determine cycles and non-terminal nodes
        explored = set()

        # traverse all nodes
        for i in range(len(graph)): 
            if i not in terms: 
                self.dfs(i, graph, terms, explored)
        
        # convert to list and return
        sol = list(terms)
        sol.sort()

        return sol
    
    def dfs(self, curr, graph, terms, explored): 
        # case where there is a cycle in list, thus not safe
        if curr not in terms and curr in explored: 
            return False

        # visit node
        explored.add(curr)
        if curr in terms: 
            return True

        # if all neighbor paths return True, node is safe
        safe = True
        for neigh in graph[curr]: 
            if not self.dfs(neigh, graph, terms, explored): 
                safe = False
        
        if safe: 
            # add safe node to terms as you go
            terms.add(curr)
            return True
        else: 
            return False
