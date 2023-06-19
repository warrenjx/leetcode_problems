class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        max_alt = 0
        curr = 0
        
        # keep track of sum as you go
        for num in gain: 
            curr += num

            if curr > max_alt: 
                max_alt = curr

        return max_alt
