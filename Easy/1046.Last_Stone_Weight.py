class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # create a max heap by inverting all the weights
        for i in range(len(stones)): 
            stones[i] = -stones[i]
        
        while len(stones) > 1: 
            heapify(stones)

            # get 2 largest stones
            num1 = heappop(stones)
            num2 = heappop(stones)

            # combine them
            new = min(num1, num2) - max(num1, num2)
            if new != 0:
                stones.append(new)
        
        # either return last value or 0
        if stones: 
            return -stones[0]
        else: 
            return 0
