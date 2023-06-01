class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # if a 1 by 1 grid
        if len(grid) == 1 and len(grid[0]) == 1: 
            if grid[0][0] == 1: 
                return -1
            else: 
                return 1
        
        # initialize the stack that will be used to keep track of each wave of BFS-ing
        stack = deque()
        if grid[0][0] == 0: 
            stack.append((0, 0))
        else: 
            return -1

        width = 1
        time = 0
        while stack:
            time += 1
            next_width = 0
            for i in range(width): 
                y, x = stack.popleft()
                
                # if traversed the end goal
                if (y == len(grid) - 1) and (x == len(grid[0]) - 1): 
                    return time

                # check all 8 possible ways for it to spread
                if (y > 0) and grid[y - 1][x] == 0: 
                    next_width += 1
                    stack.append((y - 1, x))
                    grid[y - 1][x] = 1
                if (y > 0) and (x > 0) and grid[y - 1][x - 1] == 0: 
                    next_width += 1
                    stack.append((y - 1, x - 1))
                    grid[y - 1][x - 1] = 1
                if (x > 0) and grid[y][x - 1] == 0: 
                    next_width += 1
                    stack.append((y, x - 1))
                    grid[y][x - 1] = 1
                if (y < len(grid) - 1) and (x > 0) and grid[y + 1][x - 1] == 0: 
                    next_width += 1
                    stack.append((y + 1, x - 1))
                    grid[y + 1][x - 1] = 1
                if (y < len(grid) - 1) and grid[y + 1][x] == 0: 
                    next_width += 1
                    stack.append((y + 1, x))
                    grid[y + 1][x] = 1
                if (y < len(grid) - 1) and (x < len(grid[0]) - 1) and grid[y + 1][x + 1] == 0: 
                    next_width += 1
                    stack.append((y + 1, x + 1))
                    grid[y + 1][x + 1] = 1
                if (x < len(grid[0]) - 1) and grid[y][x + 1] == 0: 
                    next_width += 1
                    stack.append((y, x + 1))
                    grid[y][x + 1] = 1
                if (y > 0) and (x < len(grid[0]) - 1) and grid[y - 1][x + 1] == 0: 
                    next_width += 1
                    stack.append((y - 1, x + 1))
                    grid[y - 1][x + 1] = 1

                width = next_width

        return -1 
