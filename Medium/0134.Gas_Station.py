class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        # create array of the sums of the gas cost and amount at each station
        gas_diff = [0] * n
        for i in range(n): 
            gas_diff[i] = gas[i] - cost[i]

        # the problem can now be solved like a prefix sum problem
        # idx keeps track of what index the ideal start is
        # starts at -1 because its actually the end of the smallest prefix sum
        idx = -1

        pref_sum = 0

        # holds the smallest prefix sum value
        min_gas = 0

        for i in range(n): 
            pref_sum += gas_diff[i]

            # update idx to be the index of the end of the minimum prefix sum
            if pref_sum <= min_gas: 
                min_gas = pref_sum
                idx = i
            
        if pref_sum >= 0: # if prefix sum is not negative, it is possible
            if idx + 1 == n: 
                return 0
            else: 
                return idx + 1
        else: # if negative it is not possible
            return -1
