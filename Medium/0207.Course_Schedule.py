class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj_list = {}
        visited = []

        # fill in adjacency list from prerequisites
        for course in prerequisites: 
            if course[1] in adj_list: 
                adj_list[course[1]].append(course[0])
            else: 
                adj_list[course[1]] = [course[0]]

        # recursively run dfs on all unexplored nodes in adjacency list
        explored = []
        for node in adj_list.keys(): 
            if node not in explored:
                explored.append(node)
                if self.dfs(node, adj_list, visited, explored): 
                    return False
        
        return True

    def dfs(self, node, adj_list, visited, explored): 
        visited.append(node)

        # base case for recursion
        if node not in adj_list: 
            visited.pop()
            return False

        # recursion part on each possible prereq path from node
        for path in adj_list[node]: 
            if path in visited: 
                return True
            else: 
                if path not in explored and self.dfs(path, adj_list, visited, explored): 
                    return True
                explored.append(path)

        visited.pop()
        return False