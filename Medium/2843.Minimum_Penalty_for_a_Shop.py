class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        c = 0 # penalty ccount for the closed days
        # increase penalty for every customer 
        for cust in customers: 
            if cust == 'Y': 
                c += 1
        
        o = 0 # penalty count for open days
        sol = 0 # index of best time to be open
        
        min_val = o + c # minimum amount of penalties

        for i in range(len(customers)): 
            # both c and o are prefix sums
            if customers[i] == 'Y': 
                c -= 1 # if open, decrease closed penalty
            else: 
                o += 1 # if no customers come in, increase open penalty

            # check if a new minimum penalty has occurred
            if o + c < min_val:
                sol = i + 1
                min_val = o + c

        return sol
