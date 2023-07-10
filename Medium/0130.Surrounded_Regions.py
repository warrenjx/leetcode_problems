class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # define variables to make it easier
        self.rows = len(board)
        self.cols = len(board[0])

        # change all 'O' to a temporary value 'T'
        for i in range(self.rows): 
            for j in range(self.cols): 
                if board[i][j] == 'O': 
                    board[i][j] = 'T'

        # if 'T' is reachable from top or bottom change it back to 'O'
        for i in range(self.rows): 
            if board[i][0] == 'T': 
                self.dfs(board, i, 0)
            if board[i][self.cols - 1] == 'T': 
                self.dfs(board, i, self.cols - 1)
        
        # is 'T' is reachable from left or right side change it back to 'O'
        for j in range(self.cols): 
            if board[0][j] == 'T': 
                self.dfs(board, 0, j)
            if board[self.rows - 1][j] == 'T': 
                self.dfs(board, self.rows - 1, j)
        
        # Change all remaining 'T' to X as they would have been surrounded
        for i in range(self.rows): 
            for j in range(self.cols): 
                if board[i][j] == 'T': 
                    board[i][j] = 'X'

        return


    def dfs(self, grid, i, j): 
        stack = deque()
        stack.append((i, j))

        while stack: 
            y, x = stack.pop()

            # out of bounds
            if y < 0 or x < 0 or y >= self.rows or x >= self.cols: 
                continue
            # not O
            if grid[y][x] != 'T': 
                continue
            
            # visit
            grid[y][x] = 'O'

            stack.append((y - 1, x))
            stack.append((y + 1, x))
            stack.append((y, x - 1))
            stack.append((y, x + 1))
        
        return
