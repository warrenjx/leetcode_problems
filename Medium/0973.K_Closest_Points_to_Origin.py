class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # create heap of format (distance, (x coord, y coord))
        heap = []
        heapify(heap)

        for x, y in points: 
            dist = ((x ** 2) + (y ** 2)) ** 0.5

            heappush(heap, (dist, (x, y)))

        sol = []
        # get the k least elements in heap
        for i in range(k): 
            sol.append(heappop(heap)[1])

        return sol
