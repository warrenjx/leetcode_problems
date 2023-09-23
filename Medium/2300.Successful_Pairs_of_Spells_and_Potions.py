class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(potions)
        # sort potions because thats what we BS on
        potions.sort()
        
        sol = []
        for spell in spells: 
            # binary search on potions to see what is index of lowest possible potion
            hi = n - 1
            lo = 0
            while lo <= hi: 
                mid = (hi + lo) // 2
                # calculate potion spell combo 
                if (potions[mid] * spell) >= success: 
                    hi = mid - 1
                else: 
                    lo = mid + 1
            
            # n - lowest possible index is the amount of successful spells
            sol.append(n - lo)
        
        return sol
