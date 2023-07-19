class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # edge case: only 1 interval
        if len(intervals) == 1: 
            return 0

        # get intervals sorted by start
        intervals.sort(key=lambda x:x[0])

        sol = 0

        for i in range(1, len(intervals)):
            # if there is an overlap
            if intervals[i][0] < intervals[i - 1][1]: 
                sol += 1

                # change later interval to smaller of the 2, simulates removing the larger one
                if intervals[i][1] > intervals[i - 1][1]: 
                    intervals[i][1] = intervals[i - 1][1]

        return sol
