class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort intervals makes it much easier
        intervals.sort(key = lambda x: x[0])

        sol = []
        
        # represents the current start and end of intervals
        curr_s, curr_e = intervals[0]

        # check rest of intervals
        for i in range(1, len(intervals)): 
            if curr_e >= intervals[i][0]: # overlap detected
                # update end of current interval
                curr_e = max(curr_e, intervals[i][1])
            else: # no overlap
                # add current interval
                sol.append([curr_s, curr_e])

                # update current interval to intervals[i]
                curr_s, curr_e = intervals[i]
        
        # add final interval
        sol.append([curr_s, curr_e])

        return sol
