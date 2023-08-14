class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # these variables represent if the first, second, and third item in target can be reached
        fir = False
        sec = False
        thr = False

        # check each triplet for matches
        for trip in triplets: 
            # if any term in triplet is greater than target term, its invalid to be used, skip
            if trip[0] > target[0]: 
                continue
            elif trip[1] > target[1]: 
                continue
            elif trip[2] > target[2]: 
                continue
            
            # if any term in triplet match then its valid since others are less than target
            if trip[0] == target[0]: 
                fir = True
            if trip[1] == target[1]: 
                sec = True
            if trip[2] == target[2]: 
                thr = True
        
        # if all are true, target can be formed
        return fir == sec == thr == True
        
