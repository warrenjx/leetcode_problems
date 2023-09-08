class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # start with base case of size 1
        sol = [[1]]
        # if it is length 2
        if numRows > 1: 
            sol.append([1, 1])
        
        # the rest of the rows can be built algorithmically
        for i in range(2, numRows): 
            curr = [1] # first of every row is always 1
            # fill in interior based off of previous row term sums
            for j in range(i - 1): 
                curr.append(sol[i - 1][j] + sol[i - 1][j + 1])
            curr.append(1) # end of every row is always 1
            
            sol.append(curr)

        return sol
