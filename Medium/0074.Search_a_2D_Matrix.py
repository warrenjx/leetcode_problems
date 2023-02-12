class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = len(matrix) - 1

        # finds appropriate row for num
        while row >= 0 and matrix[row][0] > target:
            row -= 1
        
        # checks row for target num
        for num in matrix[row]:
            if num == target: 
                return True

        return False
                 