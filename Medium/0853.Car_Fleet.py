class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        # have it sorted by starting position as cars cannot pass
        pairs = zip(position, speed)
        pairs.sort(key=lambda x: x[0], reverse=True)

        if len(pairs) <= 1: 
            return 1

        sol = 1
        arrival_time = float(target - pairs[0][0]) / pairs[0][1]
        
        idx = 1
        while idx < len(pairs): 
            curr_arrival_time = float(target - pairs[idx][0]) / pairs[idx][1]

            # if the current arrival time is greater than previous, must be new fleet
            if curr_arrival_time > arrival_time: 
                arrival_time = curr_arrival_time
                sol += 1
            
            idx += 1
        
        return sol
