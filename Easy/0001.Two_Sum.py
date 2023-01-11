class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # dictionary as hashmap
        hash_map = {}

        for idx, num in enumerate(nums):
            # if the desired complement to num is in hashmap 
            if (target - num) in hash_map: 
                return hash_map[target - num], idx
            
            #if not solution add to hashmap incase it matches with later values
            hash_map[num] = idx