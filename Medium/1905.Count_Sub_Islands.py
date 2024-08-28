class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        n = len(grid1)
        m = len(grid1[0])

        sol = 0

        # check each square in the grid
        for i in range(n): 
            for j in range(m): 

                # if not land doesnt matter
                if grid2[i][j] == 0: 
                    continue
                
                # bfs from the square if land
                q = deque()
                q.append((i, j))

                # at first the island is considered a sub island
                sub = True
                while q: 
                    y, x = q.popleft()

                    # invalid conditions
                    if (y < 0) or (y >= n): # if outside boundaries of grid 
                        continue
                    elif (x < 0) or (x >= m): 
                        continue
                    elif grid2[y][x] == 0: # if not land
                        continue     

                    # if land is not land in grid1, no longer a sub island
                    if sub and grid1[y][x] == 0: 
                        sub = False
                    
                    # set tile as visited
                    grid2[y][x] = 0

                    # visit neighbors
                    q.append((y, x - 1))
                    q.append((y - 1, x))
                    q.append((y, x + 1))
                    q.append((y + 1, x))

                # if sub remained valid throughout bfs it is a sub island
                if sub: 
                    sol += 1
    
        return sol
                
