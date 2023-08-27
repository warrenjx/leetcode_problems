class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # convenience variables
        m = len(maze)
        n = len(maze[0])

        # directions of travel in tuple, makes code simpler
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # the current distance from starting position
        level = -1 # start at -1 because completion metric is when you leave the maze

        # use queue rather than recursion
        q = deque()
        q.append(entrance) # seed the start

        while q: 
            # go by wave to make keeping track of level easier
            wave = len(q)

            for i in range(wave): 
                y, x = q.popleft()

                # if curr isnt in the maze
                if not (0 <= y < m and 0 <= x < n): 
                    if level > 0: # if still 0, that means left from entrance position
                        return level
                    
                    continue
                elif maze[y][x] == "+": # dont visit already visited nodes
                    continue
                
                # mark node as visited
                maze[y][x] = "+"

                # visit neihhbors using direction arrays
                for d_y, d_x in dirs: 
                    q.append((y + d_y, x + d_x))
            
            # increment level away from entrance
            level += 1
        
        # no exit found
        return -1
