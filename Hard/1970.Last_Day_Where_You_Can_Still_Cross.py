class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        # binary search cells until it gets blocked
        lo = 0
        hi = len(cells) - 1

        while hi >= lo: 
            mid = (hi + lo) // 2

            # row is y axis, col is x axis
            matrix = [[0] * col for i in range(row)]

            # populate matrix with water
            for i in range(mid): 
                matrix[cells[i][0] - 1][cells[i][1] - 1] = 1
            
            # dfs to check if there is path through
            stack = deque()
            passed = False
            # add starting row to stack
            for i in range(col): 
                if matrix[0][i] == 0: 
                    stack.append((0, i))
            
            while stack: 
                curr_y, curr_x = stack.pop()

                # end condition
                if curr_y == row - 1: 
                    passed = True
                    break
                
                # mark current as visited: 
                matrix[curr_y][curr_x] = 1

                # explore neighbors
                if curr_y > 0 and matrix[curr_y - 1][curr_x] == 0: 
                    stack.append((curr_y - 1, curr_x))
                if curr_y < row - 1 and matrix[curr_y + 1][curr_x] == 0: 
                    stack.append((curr_y + 1, curr_x))
                if curr_x > 0 and matrix[curr_y][curr_x - 1] == 0: 
                    stack.append((curr_y, curr_x - 1))
                if curr_x < col - 1 and matrix[curr_y][curr_x + 1] == 0: 
                    stack.append((curr_y, curr_x + 1))

            # change hi/lo if there is or isnt a path through
            if passed: 
                lo = mid + 1
            else: 
                hi = mid - 1
        
        # return hi not lo as it is last time it passed
        return hi
