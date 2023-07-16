class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge cases for small neighborhoods, can only rob 1 house
        if len(nums) < 4: 
            return max(nums)
        
        # create 2 sets of dp, one excluding first house, one excluding last house
        dp_1 = nums[0:3]
        dp_1[2] += dp_1[0]
        
        dp_2 = nums[1:4]
        dp_2[2] += dp_2[0]

        # same process as House Robber 1, but do it for both
        for i in range(3, len(nums) - 1): 
            dp_1.append(max(dp_1[i - 2], dp_1[i - 3]) + nums[i])
            dp_2.append(max(dp_2[i - 2], dp_2[i - 3]) + nums[i + 1])
        
        # choose max from both dp sets
        return max(max(dp_1[-1], dp_1[-2]), max(dp_2[-1], dp_2[-2]))
