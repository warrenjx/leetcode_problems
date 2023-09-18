class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # convenience variables
        m = len(mat)
        n = len(mat[0])

        # format of heap entries: (count, index)
        heap = []

        # populate heap
        for i in range(m): 
            ct = 0
            for j in range(n): 
                if mat[i][j] == 1: 
                    ct += 1
                else: 
                    break
            
            heappush(heap, (ct, i))
        
        sol = []

        # pop the least k elements
        for i in range(k): 
            sol.append(heappop(heap)[1])
        
        return sol
