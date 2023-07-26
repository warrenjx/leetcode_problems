class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        hi = 1e9 # need super high max value because of some testcases
        lo = 1 # cant go below 1 speed

        # default value, if its not possible to reach in time will be returned
        min_speed = -1
        
        # normal binary search
        while lo <= hi: 
            mid = (hi + lo) // 2

            # if arrival time is less than or equal to goal
            if self.calc_time(dist, mid) <= hour: 
                # only update speed if it is possible
                min_speed = int(mid)
                hi = mid - 1
            else: # too slow, need to increase speed
                lo = mid + 1

        return min_speed
    
    # function calculates the arrival speed of the train with stops
    def calc_time(self, dist, speed): 
        time = 0

        # calculate each distance except the last one
        for i in range(len(dist) - 1): 
            # do ceiling division because trains can only leave at integer hours
            time += (dist[i] + speed - 1) // speed
        
        # calculate last one without ceiling because no other train to catch
        time += float(dist[-1]) / speed

        return time
