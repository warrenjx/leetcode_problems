class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        # same as H-Index 1 but with negative indexing
        for i in range(1, len(citations) + 1): 
            if citations[-i] < i: 
                 return i - 1
        
        return len(citations)
      
