class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sol = [0] * len(nums)
        
        # positive nums at even indeces
        pos_i = 0
        # negative nums at odd indeces
        neg_i = 1

        # add the nums in chronological order
        for num in nums: 
            if num > 0: # positives at pos idx
                sol[pos_i] = num
                pos_i += 2
            else: # negatives at neg idx
                sol[neg_i] = num
                neg_i += 2
        
        return sol
