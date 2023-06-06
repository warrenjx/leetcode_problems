class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        arr.sort()

        gap = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != gap: 
                return False
        
        return True
