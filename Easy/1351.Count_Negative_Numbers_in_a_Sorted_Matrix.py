class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        sol = 0

        for i in range(len(grid)): 
            for j in range(len(grid[i])):
                # once a negative is found, can assume the rest are negative 
                if grid[i][j] < 0: 
                    sol += len(grid[i]) - j
                    break
        
        return sol
