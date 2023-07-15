class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # start with array containing first 2 costs, build rest of the cases off of these
        min_costs = cost[0:2]

        for i in range(2, len(cost)): 
            # the price of a step is the min between the past 2 steps plus current cost
            min_costs.append(min(min_costs[i - 1], min_costs[i - 2]) + cost[i])

        # return the min between the steps you can exit array from
        return min(min_costs[-1], min_costs[-2])
