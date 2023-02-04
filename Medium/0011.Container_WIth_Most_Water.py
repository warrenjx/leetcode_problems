class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 1: 
            return height[0]
        
        max_vol = 0
        left = 0
        right = len(height) - 1

        # moves pointers inwards from edges
        while left < right: 
            vol = min(height[left], height[right]) * (right - left)

            if vol > max_vol: 
                max_vol = vol
            
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        
        return max_vol