class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sorting intervals makes it significantly easier
        intervals.sort(key = lambda x: x[0])

        sol = 0

        # start iterating at 1 because we compare to interval before
        for i in range(1, len(intervals)): 
            # if there is an overlap
            if intervals[i][0] < intervals[i - 1][1]: 
                # increment solution
                sol += 1

                # set end of current interval to min, simulating removing the LARGER interval
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])

        return sol
