class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # visited rooms
        visited = set()

        # stack for iteration over recursion
        stack = deque()
        stack.append(0) # always start at room 0

        while stack: 
            curr = stack.pop()

            # visit process
            if curr in visited: # dont visit visited rooms
                continue
            else: # add room to visited
                visited.add(curr)
            
            # visit neighbors
            for key in rooms[curr]: 
                stack.append(key)

        # if they are the same length, visited all rooms from 0
        return len(visited) == len(rooms)
