class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # sets to hold the rows and columsn to set as zero
        z_cols = set()
        z_rows = set()

        # populate the sets
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])): 
                if matrix[row][col] == 0: 
                    z_cols.add(col)
                    z_rows.add(row)

        # zero out the rows and columns
        for col in z_cols: 
            for i in range(len(matrix)): 
                matrix[i][col] = 0
        for row in z_rows: 
            for i in range(len(matrix[row])): 
                matrix[row][i] = 0

        return
