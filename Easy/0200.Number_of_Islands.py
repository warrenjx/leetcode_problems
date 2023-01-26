class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: 
            return 0
        
        count = 0
        
        # run recursive dfs on every node on grid if it is a 1
        for y in range(len(grid)): 
            for x in range(len(grid[y])): 
                if grid[y][x] == "1": 
                    self.dfs(grid, x, y)
                    count += 1

        return count

    def dfs(self, grid, x, y): 
        
        # if is part of an island
        if (grid[y][x] == "1"): 
            grid[y][x] = "0"

            # check all adjacent nodes if part of island
            if (y > 0): 
                self.dfs(grid, x, y - 1)
            if (y < len(grid) - 1): 
                self.dfs(grid, x, y + 1)
            if (x > 0): 
                self.dfs(grid, x - 1, y)
            if (x < len(grid[y]) - 1): 
                self.dfs(grid, x + 1, y)
        
        return
        