class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1

        # bitmap
        bitmap = 0
        for num in nums: 
            bitmap |= (1 << num)

        # only one missing from bitmap is the target
        for i in range(n): 
            if not bitmap & (1 << i): 
                return i

        return -1
        
