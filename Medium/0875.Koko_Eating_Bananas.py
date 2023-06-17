class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        hi = max(piles)
        lo = 1

        # binary search to find correct value for h
        while lo < hi: 
            mid = (hi + lo) // 2

            # calculate current time of h
            curr_h = 0
            for pile in piles: 
                curr_h += (pile - 1) // mid + 1
            
            if curr_h > h: 
                lo = mid + 1
            else: 
                hi = mid
        
        return lo
