class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0

        # pop all occurances of val
        while i < len(nums): 
            if (nums[i] == val): 
                nums.pop(i)
                i -= 1
            
            i += 1
