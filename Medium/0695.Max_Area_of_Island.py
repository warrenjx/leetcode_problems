class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        tots = [0]

        # calls DFS on every cell that is 1
        for y in range(len(grid)): 
            for x in range(len(grid[y])): 
                if grid[y][x] == 1: 
                    tot = self.dfs(grid, x, y, 0)
                    # area of current island just dfs'ed
                    tots.append(tot)
        
        return max(tots)

    def dfs(self, grid, x, y, tot): 
        if (grid[y][x] == 1): 
            # visit cell then "add to visited queue"
            tot += 1
            grid[y][x] = 0

            # check adjacent cells 
            if (x < len(grid[y]) - 1): 
                tot = self.dfs(grid, x + 1, y, tot)
            if (x > 0): 
                tot = self.dfs(grid, x - 1, y, tot)
            if (y < len(grid) - 1): 
                tot = self.dfs(grid, x, y + 1, tot)
            if (y > 0): 
                tot = self.dfs(grid, x, y - 1, tot)

        return tot