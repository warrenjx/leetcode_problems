class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # the maximum index that can be reached from current position
        # starts at 1 to begin with
        max_reachable = 1

        for i in range(len(nums)): 
            # only update jump distance if you can jump there
            if i < max_reachable: 
                # increase jump distance if current position allows you to
                max_reachable = max(max_reachable, i + nums[i] + 1)

        return max_reachable >= len(nums)
