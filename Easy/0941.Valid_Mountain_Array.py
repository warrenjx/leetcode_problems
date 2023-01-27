class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if (len(arr) < 3): 
            return False
        
        if (arr[1] <= arr[0]): 
            return False

        increasing = True
        for i in range(2, len(arr)): 
            if increasing: 
                if arr[i] < arr[i - 1]: 
                    increasing = False
                if arr[i] == arr[i - 1]: 
                    return False
            else: 
                if arr[i] >= arr[i - 1]: 
                    return False
        
        if increasing: 
            return False

        return True