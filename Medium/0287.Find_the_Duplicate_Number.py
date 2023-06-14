class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        fast = 0
        slow = 0

        # floyd cycle detection algorithm
        while True: 
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow: 
                break
        
        # set one back to beginning and move at same pace, will collide at duplicate
        slow = 0
        while True: 
            if fast == slow: 
                break

            fast = nums[fast]
            slow = nums[slow]
        
        return fast
