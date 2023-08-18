class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # edge case: no intervals
        if not intervals: 
            return [newInterval]

        # convenience variable
        n = len(intervals)
        sol = []

        # gets incremented as intervals is traversed
        idx = 0

        # add all the intervals before the new interval first
        while idx < n: 
            if intervals[idx][1] < newInterval[0]: # interval is intact before new interval
                sol.append(intervals[idx])
            elif intervals[idx][0] > newInterval[1]: # new interval is not overlapping
                # just insert new interval with no modifications
                sol.append(newInterval)

                # add the rest of the intervals and return
                for i in range(idx, n): 
                    sol.append(intervals[i])

                return sol
            else: # new interval overlaps
                break
            
            idx += 1

        # edge case, all of intervals is before newInterval
        if idx == n: 
            sol.append(newInterval)

            return sol
        
        # represents the current start and end of the interval
        curr_s = min(newInterval[0], intervals[idx][0])
        curr_e = max(newInterval[1], intervals[idx][1])

        # add intervals, check if they overlap now that new interval is in
        while idx < n: 
            if intervals[idx][0] > curr_e: # no overlap
                # add the current interval
                sol.append([curr_s, curr_e])

                # update the current interval to intervals[idx]
                curr_s = intervals[idx][0]
                curr_e = intervals[idx][1]
            else: # overlap, update end of current interval
                curr_e = max(curr_e, intervals[idx][1])

            idx += 1
        
        # add final interval
        sol.append([curr_s, curr_e])
        
        return sol
        
