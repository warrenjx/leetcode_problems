class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # build hashmap representing a number and the amount of occurances in nums
        hashmap = {}
        for num in nums: 
            if num in hashmap: 
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        sol = 0

        # check each number in hashmap for a sum pair equal to k
        for num in hashmap: 
            if k - num in hashmap: 
                if k - num == num: # if num is k / 2 it gets divided by 2
                    sol += hashmap[num] // 2
                else: # else minimum of the frequencies is chosen
                    sol += min(hashmap[num], hashmap[k - num])

                # set the numbers to 0 so they don't get double counted
                hashmap[num] = 0
                hashmap[k - num] = 0

        return sol
