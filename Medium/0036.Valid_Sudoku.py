class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # rows
        for i in range(0, 9): 
            tester = [0] * 9
            for j in board[i]: 
                if j.isnumeric(): 
                    if tester[int(j) - 1] != 0: 
                        return False
                    else: 
                        tester[int(j) - 1] += 1
            
        # columns
        for i in range(0, 9): 
            tester = [0] * 9
            for j in range(0, 9): 
                if board[j][i].isnumeric(): 
                    if tester[int(board[j][i]) - 1] != 0: 
                        return False
                    else: 
                        tester[int(board[j][i]) - 1] += 1
        
        # 3 x 3 sub boxes
        for idx in range(0, 3): 
            for jdx in range(0, 3): 
                tester = [0] * 9
                for i in range(0, 3): 
                    for j in range(0, 3): 
                        if board[i + 3 * idx][j + 3 * jdx].isnumeric(): 
                            if tester[int(board[i + 3 * idx][j + 3 * jdx]) - 1] != 0: 
                                return False
                            else: 
                                tester[int(board[i + 3 * idx][j + 3 * jdx]) - 1] += 1
                
        return True