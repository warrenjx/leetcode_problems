class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # create hashmap mapping numbers to their frequencies
        hashmap = {}
        for num in arr: 
            if num in hashmap: 
                hashmap[num] += 1
            else: 
                hashmap[num] = 1
        
        # freqs is array containing frequencies of numbers
        freqs = hashmap.values()
        freqs.sort()
        
        # remove numbers in order of least frequent to most frequent
        i = 0
        while k > 0: 
            if k == freqs[i]: 
                k = 0
                freqs[i] = 0
            elif k > freqs[i]: 
                k -= freqs[i]
                freqs[i] = 0
            else: # k < freqs
                freqs[i] -= k
                k = 0

            i += 1
        
        # count number of nonzero frequencies
        sol = 0
        for freq in freqs: 
            if freq > 0: 
                sol += 1

        return sol
