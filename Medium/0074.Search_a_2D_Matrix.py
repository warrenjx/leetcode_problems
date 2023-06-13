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
                
# Binary Search SOLUTION: 
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # binary search rows to find correct row
        l = 0
        r = len(matrix) - 1

        row = 0
        while l <= r: 
            mid = (l + r) // 2

            if matrix[mid][0] > target: 
                r = mid - 1
            else: 
                l = mid + 1
        row = r
        
        # binary search the row to find correct number
        l = 0
        r = len(matrix[row]) - 1

        while l <= r: 
            mid = (l + r) // 2

            if matrix[row][mid] == target: 
                return True
            elif matrix[row][mid] > target: 
                r = mid - 1
            else: 
                l = mid + 1

        return False
