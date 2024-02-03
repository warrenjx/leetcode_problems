class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        # dp holds the minimum number of moves needed to get to a position
        dp = [[999999] * n for i in range(n)]
        
        # stack holds active positions
        stack = deque()
        stack.append((1, 0))

        # BFS through the board
        while stack: 
            pos, moves = stack.popleft()

            # off of the board
            if pos > n ** 2: 
                continue
            
            # convert positon to coordinates
            y, x = self.pos_to_coord(pos, n)
            # if coordinates are snake or ladder move to end position
            if board[y][x] != -1: 
                pos = board[y][x]
                y, x = self.pos_to_coord(pos, n)

            if dp[y][x] <= moves: # if already seen before, no need
                continue
            else: # set dp with new lowest value
                dp[y][x] = moves

            # queue the new possible moves
            for i in range(1, 7): 
                stack.append((pos + i, moves + 1))

        # check solution position
        sol = -1
        if n % 2 == 0: 
            sol = dp[0][0]
        else: 
            sol = dp[0][n - 1]
        
        # if no solution found, return -1
        if sol == 999999: 
            return -1
        else: 
            return sol
    
    # function to convert numerical position to coordinates on the board
    def pos_to_coord(self, pos, n): 
        # start is bottom left corner
        y = n - 1
        x = 0

        # get the displacement on the board
        row = (pos - 1) // n
        col = (pos - 1) % n

        y -= row

        # change how the displacement is used based on row
        if n % 2 == 0: 
            if y % 2 == 1: # counting downwards
                x = col
            else: # counting upwards
                x = n - col - 1
        else: 
            if y % 2 == 1: # counting upwards
                x = n - col - 1
            else: # counting downwards
                x = col

        return (y, x)
        
