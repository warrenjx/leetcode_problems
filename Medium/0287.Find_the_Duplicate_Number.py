class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # FLoyd's cycle detection algorithm
        fast = 0
        slow = 0

        while True: 
            # if there is a cycle, the will overlap once
            fast = nums[nums[fast]]
            slow = nums[slow]

            if nums[fast] == nums[slow]: 
                # after they overlap, set one to beginning
                slow = 0

                while True: 
                    # increment both by 1, when they meet again it will be the duplicate
                    if nums[fast] == nums[slow]: 
                        return nums[fast]
                    
                    slow = nums[slow]
                    fast = nums[fast]
        
        # no returns needed out here because it is required to have a dup