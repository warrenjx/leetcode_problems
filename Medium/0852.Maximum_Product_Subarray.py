class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: partition the array into groups of nonzero numbers
        pos_ct = 0
        neg_ct = 0
        # format: [(end of partition zero index, num of positives, num of negatives), ...]
        zeros_p = []
        
        sol = -999999 # placeholder
        for i in range(len(nums)): 
            if nums[i] > 0: 
                pos_ct += 1
            elif nums[i] < 0: 
                neg_ct += 1
            else: 
                zeros_p.append((i, pos_ct, neg_ct))

                neg_ct = 0
                pos_ct = 0
                sol = 0 # in case there is a case with all negative numbers
        
        # add to the last numbers of the array to partition
        if nums[-1] != 0: 
            zeros_p.append((len(nums), pos_ct, neg_ct))
        
        start = 0
        for end, pos, neg in zeros_p: 
            # skip any zeros for partition calculations
            if nums[start] == 0: 
                start += 1
                
            if neg == pos == 0: # empty partition
                sol = max(sol, 0)
            elif neg % 2 == 0: # even number of negatives in this partition, multiply all numbers together
                curr = 1
                for i in range(start, end): 
                    curr *= nums[i]
                
                sol = max(sol, curr)
            elif pos == 0 and neg == 1: # for singular negative numbers
                for i in range(start, end): 
                    sol = max(sol, nums[i])
            else: # add number of negatives, find best subarray in partition
                # separate digits into products of positives interspaced with negatives
                parcels = []
                prod = 1
                for i in range(start, end): 
                    if nums[i] > 0: 
                        prod *= nums[i]
                    else: 
                        parcels.append(prod)
                        parcels.append(nums[i])
                        prod = 1

                # add last parcel if there is no last negative number
                if nums[end - 1] > 0: 
                    parcels.append(prod)
                
                if neg == 1: # if only 1 negative
                    # max will just be the largest of the positive parcels
                    sol = max(sol, max(parcels))
                else: # if 3, 5, 7, etc. negatives

                    # the largest will be the section excluding the first or last negatives
                    temp_prod_1 = 1
                    temp_prod_2 = 1

                    # calculate top index for section excluding last negative
                    top = 0
                    for i in range(len(parcels) - 1, -1, -1): 
                        if parcels[i] < 0: 
                            top = i
                            break
                    # calculate bottom index for section excluding first negative
                    bot = 0
                    for i in range(len(parcels)): 
                        if parcels[i] < 0: 
                            bot = i + 1
                            break

                    # calculate the 2 section products and compare to current solution
                    for i in range(0, top): 
                        temp_prod_1 *= parcels[i]
                    for i in range(bot, len(parcels)): 
                        temp_prod_2 *= parcels[i]

                    sol = max(sol, temp_prod_1, temp_prod_2)
            
            # move onto next partition
            start = end

        return sol
