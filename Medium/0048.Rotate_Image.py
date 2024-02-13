class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # traverse one quarter of matrix
        for i in range(n // 2): 
            for j in range(-(n // -2)): 
                # swap mega line
                matrix[i][j], matrix[j][-i - 1], matrix[-i - 1][-j - 1], matrix[-j - 1][i] = matrix[-j - 1][i], matrix[i][j], matrix[j][-i - 1], matrix[-i - 1][-j - 1]
