class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        hashtable = {}

        # add all the rows to a hashtable, value is how many there are
        for row in grid: 
            if tuple(row) in hashtable: 
                hashtable[tuple(row)] += 1
            else: 
                hashtable[tuple(row)] = 1

        # check the columns against the row and increment the solution
        sol = 0
        for i in range(len(grid[0])):
            curr = []
            for j in range(len(grid)): 
                curr.append(grid[j][i])
            
            curr = tuple(curr)
            if curr in hashtable:
                sol += hashtable[curr]
        
        return sol
