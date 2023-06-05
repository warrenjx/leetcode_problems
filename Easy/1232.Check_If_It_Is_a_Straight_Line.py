class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        if len(coordinates) == 2: # only 2 points
            return True
        
        # find slope between first 2 points
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]

        for i in range(2, len(coordinates)):
            # current slope  
            curr_rise = coordinates[i][1] - coordinates[i - 1][1]
            curr_run = coordinates[i][0] - coordinates[i - 1][0]

            # should result in same number if slopes are the same
            if curr_rise * run != curr_run * rise: 
                return False
        
        return True
