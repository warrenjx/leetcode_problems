class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # negate all numbers so default heap makes it a "max" heap
        for i in range(len(gifts)): 
            gifts[i] = -gifts[i]
        heapify(gifts)

        # pop largest number and square root it, then push it back on k times
        for i in range(k): 
            new = heappop(gifts)
            heappush(gifts, -int((-new) ** 0.5))
        
        # sum the magnitude of remaining gifts
        sol = 0
        for num in gifts: 
            sol -= num

        return sol
