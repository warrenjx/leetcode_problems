class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0: # edge case: no flowers need to be planted
            return True
        if len(flowerbed) == 1: # edge case: only 1 pot to plant in
            return flowerbed[0] == 0

        ct = 0
        # check the first term to plant
        if flowerbed[0] == flowerbed[1] == 0: 
            ct += 1
            flowerbed[0] = 1
        # check the middle terms
        for i in range(1, len(flowerbed) - 1): 
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0: 
                ct += 1
                flowerbed[i] = 1
        # check the end terms
        if flowerbed[-2] == flowerbed[-1] == 0: 
            ct += 1
            flowerbed[-1] = 1

        return (ct >= n)
        
