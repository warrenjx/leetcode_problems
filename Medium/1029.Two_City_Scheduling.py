class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # sort by largest difference, largest difference first
        #   these ones are when choosing which city to send makes the biggest difference
        costs.sort(key=lambda x:abs(x[0] - x[1]), reverse=True)

        # for convenience
        n = len(costs) / 2

        sol = 0
        # variables to store the counts of each side
        a_ct = 0
        b_ct = 0

        # greedily choose which side to 
        for pair in costs:
            if a_ct < n and pair[0] < pair[1]: # conditions to send to city 0
                sol += pair[0]
                a_ct += 1
            elif b_ct < n and pair[1] < pair[0]: # conditions to send to city 1
                sol += pair[1]
                b_ct += 1
            else: # else send to the city that needs it the most
                if b_ct < a_ct: 
                    sol += pair[1]
                    b_ct += 1
                else: 
                    sol += pair[0]
                    a_ct += 1
        
        return sol
        
