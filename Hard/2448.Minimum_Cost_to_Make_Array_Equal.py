class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        pairs = zip(nums, cost)
        pairs.sort(key=lambda x:x[0])

        # binary search terms to find ideal
        hi = len(nums) - 1
        lo = 0
        while hi >= lo: 
            mid = (hi + lo) // 2

            # calculate cost of 2 terms next to each other
            # follow the trend, if 1 is less than 2, smaller number better, etc. 
            cost_1 = self.calc_cost(pairs, pairs[mid][0])
            cost_2 = self.calc_cost(pairs, pairs[mid][0] + 1)

            if cost_1 > cost_2: # if in a decreasing trend, increase number
                lo = mid + 1
            else: # if not, decrease number
                hi = mid - 1
        
        return self.calc_cost(pairs, pairs[lo][0])
    
    # helper function to keep code simpler
    def calc_cost(self, pairs, target): 
        target_cost = 0
        for num, cost in pairs: 
            target_cost += abs(num - target) * cost
        
        return target_cost