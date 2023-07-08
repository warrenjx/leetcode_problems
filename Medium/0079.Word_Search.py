class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(y, x, curr): 
            # base case for completion
            if curr == len(word): 
                return True

            # invalid cases
            if y < 0 or y >= rows or x < 0 or x >= cols: 
                return False
            elif board[y][x] != word[curr]: 
                return False
            
            # mark as visited
            temp = board[y][x]
            board[y][x] = "_"

            # visit neighbors
            if dfs(y - 1, x, curr + 1): 
                return True
            if dfs(y + 1, x, curr + 1): 
                return True
            if dfs(y, x - 1, curr + 1): 
                return True
            if dfs(y, x + 1, curr + 1): 
                return True

            # unmark as visited
            board[y][x] = temp

            return False

        # check all starting points
        for y in range(rows): 
            for x in range(cols): 
                if dfs(y, x, 0): 
                    return True
        
        return False
