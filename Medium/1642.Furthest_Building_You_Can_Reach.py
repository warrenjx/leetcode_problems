class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        # edge case: height only 1
        if len(heights) == 1: 
            return 0

        # heap for storing gaps in order
        heap = []

        i = 0
        while i < len(heights) - 1: 
            # calculate gap
            gap = heights[i + 1] - heights[i]

            if gap <= 0: # no bricks or ladders needed
                i += 1
                continue
            elif bricks >= gap: # can use bricks
                bricks -= gap
                # add to heap negative because its a min heap, also so it may be replaced in the future
                heappush(heap, -gap)
            elif ladders > 0: # must use a ladder
                if heap and -heap[0] > gap: # can replace a previous gap with a ladder
                    bricks += -heappop(heap)
                    bricks -= gap
                    heappush(heap, -gap)
                
                ladders -= 1
            else: 
                break

            i += 1
        
        return i
