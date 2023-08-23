class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # hashmap holds each character and their frequency
        hashmap = {}
        # populate hashmap
        for char in s: 
            if char in hashmap: 
                hashmap[char] += 1
            else: 
                hashmap[char] = 1
        
        # chars is ordered list [(char, frequency), ...]
        chars = hashmap.items()
        
        # format of heap is: [(negative frequency, char), ...]
        heap = []
        # add all terms in chars to heap
        for char, freq in chars: 
            # add freq in as negative as heap is min heap by default
            heap.append((-freq, char))
        
        heapify(heap)

        sol = ""

        # add chars until heap is 1 term or 0 terms left
        while len(heap) > 1: 
            # pop 2 chars at a time
            f1, c1 = heappop(heap)
            f2, c2 = heappop(heap)
            # add each char alternating
            sol += c1
            sol += c2

            # add chars back to heap if they haven't been used up
            if f1 < -1: 
                heappush(heap, (f1 + 1, c1))
            if f2 < -1: 
                heappush(heap, (f2 + 1, c2))
        
        # if there is an odd number of characters 
        if heap: 
            if heap[0][0] < -1: # more than 1 char, not possible to be alternating
                return ""
            else: # else just add last char
                sol += heap[0][1]

        return sol
