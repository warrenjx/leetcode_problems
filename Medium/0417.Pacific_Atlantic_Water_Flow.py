class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # variables for convenience
        rows = len(heights)
        cols = len(heights[0])

        # sea_map is grid representing what ocean every position in heights flows to
        # 1 = pacific, 2 = atlantic
        sea_map = [[0] * cols for i in range(rows)]

        # bfs from all nodes touching the pacific ocean
        queue = deque()

        # add all pacific shores to start bfs
        for i in range(rows): 
            queue.append((i, 0))
        for i in range(1, cols): 
            queue.append((0, i))
        
        while queue: 
            y, x = queue.popleft()

            # already visited by pacific
            if sea_map[y][x] == 1: 
                continue
            # visit
            sea_map[y][x] = 1

            # visit neighbors
            if y > 0 and heights[y - 1][x] >= heights[y][x]: 
                queue.append((y - 1, x))
            if y < rows - 1 and heights[y + 1][x] >= heights[y][x]: 
                queue.append((y + 1, x))
            if x > 0 and heights[y][x - 1] >= heights[y][x]: 
                queue.append((y, x - 1))
            if x < cols - 1 and heights[y][x + 1] >= heights[y][x]: 
                queue.append((y, x + 1))
        
        # list of ocean double points
        sol = []

        # now bfs atlantic sides and see where they intersect
        queue = deque()

        # add all atlantic shores to start bfs
        for i in range(rows): 
            queue.append((i, cols - 1))
        for i in range(0, cols - 1): 
            queue.append((rows - 1, i))
        
        while queue: 
            y, x = queue.popleft()

            # if already visited by atlantic
            if sea_map[y][x] == 2: 
                continue
            # if a pacific node
            if sea_map[y][x] == 1: 
                sol.append((y, x))
            # visit
            sea_map[y][x] = 2

            # visit neighbors
            if y > 0 and heights[y - 1][x] >= heights[y][x]: 
                queue.append((y - 1, x))
            if y < rows - 1 and heights[y + 1][x] >= heights[y][x]: 
                queue.append((y + 1, x))
            if x > 0 and heights[y][x - 1] >= heights[y][x]: 
                queue.append((y, x - 1))
            if x < cols - 1 and heights[y][x + 1] >= heights[y][x]: 
                queue.append((y, x + 1))
                
        return sol
