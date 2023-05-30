class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # solution is a set to avoid duplicates
        sol = set()

        # split nums into 3 lists: positives, negatives, and zeroes
        pos = []
        neg = []
        zero = []

        for num in nums: 
            if num > 0: 
                pos.append(num)
            elif num < 0: 
                neg.append(num)
            else: 
                zero.append(num)

        pos.sort()
        neg.sort()

        # create separate sets for negatives and positives for O(1) lookup
        pos_set = set(pos)
        neg_set = set(neg)

        # if there is more than 1 zero in list, add cases where num and negative num exist
        if zero: 
            for num in pos_set: 
                if (-1 * num) in neg_set: 
                    sol.add(((-1 * num), 0, num))

        # if there are more than 3 zeroes in list, add case for [0, 0, 0]
        if len(zero) >= 3: 
            sol.add((0, 0, 0))

        # find pairs of negative numbers that match with a positive number
        for i in range(len(neg)): 
            for j in range(i + 1, len(neg)): 
                target = -1 * (neg[i] + neg[j])
                if target in pos_set: 
                    sol.add((neg[i], neg[j], target))

        # find pairs of positive numbers that match with a negative number
        for i in range(len(pos)): 
            for j in range(i + 1, len(pos)): 
                target = -1 * (pos[i] + pos[j])
                if target in neg_set: 
                    sol.add((target, pos[i], pos[j]))
            
        return sol
