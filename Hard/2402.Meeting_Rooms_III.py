class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        # sort meetings by start time
        meetings.sort(key=lambda x: x[0])

        # end time heap for keeping track of occupied rooms
        end_times = []
        # heap for keeping track of open rooms
        free_rooms = []
        # initialize all rooms to free
        for i in range(n): 
            heappush(free_rooms, i)
        
        # ct[i] is the number of times room i has been used
        ct = [0] * n

        for start, end in meetings: 
            # check if any rooms have opened up at the current start time
            while end_times and start >= end_times[0][0]: 
                # free up unoccupied rooms
                end_time, open_room = heappop(end_times)
                heappush(free_rooms, open_room)

            room = -1
            # assign meeting to a room
            if free_rooms: # choose lowest number room
                room = heappop(free_rooms)
                heappush(end_times, (end, room))
            else: # choose earliest finishing room
                end_time, room = heappop(end_times)
                heappush(end_times, (end_time + end - start, room))
            
            # increment room counts
            ct[room] += 1

        # find most used room
        sol = 0
        for i in range(1, n): 
            if ct[i] > ct[sol]: 
                sol = i

        return sol
