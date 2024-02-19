class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # modify board state to reflect future changes
        for i in range(m): 
            for j in range(n): 
                neighbors = 0
                # total up direct neighbors
                if i > 0 and board[i - 1][j] >= 1: 
                    neighbors += 1
                if j > 0 and board[i][j - 1] >= 1: 
                    neighbors += 1
                if i < m - 1 and board[i + 1][j] >= 1: 
                    neighbors += 1
                if j < n - 1 and board[i][j + 1] >= 1: 
                    neighbors += 1
                # total up diagonal neighbors
                if i > 0 and j > 0 and board[i - 1][j - 1] >= 1: 
                    neighbors += 1
                if i > 0 and j < n - 1 and board[i - 1][j + 1] >= 1: 
                    neighbors += 1
                if i < m - 1 and j > 0 and board[i + 1][j - 1] >= 1: 
                    neighbors += 1
                if i < m - 1 and j < n - 1 and board[i + 1][j + 1] >= 1: 
                    neighbors += 1
                
                # encode board for future changes
                if board[i][j] == 1: 
                    # 2 means set 1 to 0
                    if neighbors < 2: 
                        board[i][j] = 2
                    elif neighbors > 3: 
                        board[i][j] = 2
                else: 
                    # -1 = set board to 1
                    if neighbors == 3: 
                        board[i][j] = -1

        # execute current changes
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == 2: 
                    board[i][j] = 0
                elif board[i][j] == -1: 
                    board[i][j] = 1
        
        return board
