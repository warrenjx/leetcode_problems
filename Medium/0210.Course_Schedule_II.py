class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # create adjacency list of graph
        adj_list = {}
        for dest, orig in prerequisites: 
            if orig in adj_list: 
                adj_list[orig].append(dest)
            else: 
                adj_list[orig] = [dest]
        
        # create an array denoting how many incoming edges for each node in graph
        in_deg = [0] * numCourses
        for course, prereq in prerequisites: 
            in_deg[course] += 1

        path = []

        # bfs the graph
        queue = deque()
        
        # all courses with no incoming edges can be started at
        for course in range(numCourses): 
            if in_deg[course] == 0: 
                queue.append(course)

        while queue: 
            curr = queue.popleft()

            # visit node
            path.append(curr)
            if curr not in adj_list: 
                continue 

            # bfs neighbors
            for neigh in adj_list[curr]: 
                in_deg[neigh] -= 1

                if in_deg[neigh] == 0: 
                    queue.append(neigh)
        
        # check if any nodes still have incoming edges (cycle in graph)
        for course in in_deg: 
            if course != 0: 
                return []
        
        return path
