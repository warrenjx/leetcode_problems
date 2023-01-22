class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # handles 1 x 1 grids
        if len(grid) == 1 and len(grid[0]) == 1: 
            if grid[0][0] == 1: 
                return -1

            return 0

        # finds all initial rotting oranges
        seeds = []
        for y in range(len(grid)): 
            for x in range(len(grid[y])): 
                if grid[y][x] == 2: 
                    seeds.append((y, x))
        
        # bfs to get the time until all possible oranges are rotted
        time = self.bfs(grid, seeds)
        
        # checking for unrotted oranges after BFS
        for y in range(len(grid)): 
            for x in range(len(grid[y])): 
                if grid[y][x] == 1: 
                    return -1

        return time

    def bfs(self, grid, seeds): 
        # no rotted oranges, either 0 or -1
        if not seeds:
            return 0
        
        visited = deque()
        time = 0

        width = 0
        for i in seeds: 
            visited.append(i)
            width += 1
        
        # mechanism is similar to iterative level-order traverse of a tree (problem 102)
        # each iteration is one time interval of rotting
        while visited:
            temp_width = 0

            # each iteration checks neighbors and adds unrotted to visited
            for i in range(width):  
                y, x = visited.popleft()

                if (x < len(grid[y]) - 1) and (grid[y][x + 1] == 1): 
                    visited.append((y, x + 1))
                    grid[y][x + 1] = 2
                    temp_width += 1
                if (x > 0) and (grid[y][x - 1] == 1): 
                    visited.append((y, x - 1))
                    grid[y][x - 1] = 2
                    temp_width += 1
                if (y < len(grid) - 1) and (grid[y + 1][x] == 1): 
                    visited.append((y + 1, x))
                    grid[y + 1][x] = 2
                    temp_width += 1
                if (y > 0) and (grid[y - 1][x] == 1): 
                    visited.append((y - 1, x))
                    grid[y - 1][x] = 2
                    temp_width += 1

            width = temp_width
            time += 1

        # - 1 because it counts the initial round as a time interval for easier coding
        return time - 1