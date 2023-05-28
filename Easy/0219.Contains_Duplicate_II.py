class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        hashmap = {}

        for i in range(len(nums)): 
            if nums[i] in hashmap: # if a duplicate is found
                if i - hashmap[nums[i]] <= k: # if previous one was <= k apart
                    return True
                hashmap[nums[i]] = i
            else: # nonduplicate, add to the hashmap
                hashmap[nums[i]] = i
        
        return False
