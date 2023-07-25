class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # very typical binary search problem
        hi = len(arr)
        lo = 0

        while lo <= hi: 
            mid = (hi + lo) // 2

            # conditions are based off of current position slope
            if arr[mid] < arr[mid + 1]: # if mid is sloping upwards, check above
                lo = mid + 1
            else: # if mid is sloping downwards, check below
                hi = mid - 1

        return lo
