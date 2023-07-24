class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # used to hold the current prefix sum starting from beginning of nums
        prefix_sum = 0
        sol = 0

        # hashtable holds prefix sums starting from the beginning of nums
        hashtable = {}
        # first prefix sum is the empty sum starting and ending at 0, occurs once
        hashtable[0] = 1

        for num in nums: 
            prefix_sum += num

            # if the current prefix sum - k is a past prefix sum
            #   means that there is a subarray that is equal to k
            if prefix_sum - k in hashtable: 
                sol += hashtable[prefix_sum - k]
            
            # add current prefix sum to hashtable
            if prefix_sum in hashtable: 
                hashtable[prefix_sum] += 1
            else: 
                hashtable[prefix_sum] = 1
        
        return sol
