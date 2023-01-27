class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # took care of circular part by doubling nums list so that it will effectively loop through twice
        mega_nums = nums + nums

        sol = [-1] * len(mega_nums)
        stack = []

        for i in range(len(mega_nums)): 
            while stack and mega_nums[i] > mega_nums[stack[-1]]: 
                curr = stack.pop()
                sol[curr] = mega_nums[i]
            
            stack.append(i)
        
        return sol[0:len(nums)]