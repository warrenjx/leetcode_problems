class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count frequencies of each element in array
        hashmap = {}
        for num in nums: 
            if num in hashmap: 
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        # keeps track of highest frequency
        curr_f = -1
        # keeps track of current total
        sol = 0
        for key, freq in hashmap.items(): 
            if freq > curr_f: # if current frequency higher than current highest, replace
                sol = freq
                curr_f = freq
            elif freq == curr_f: # else add to total
                sol += freq
        
        return sol
