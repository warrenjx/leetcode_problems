class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sorting makes it a lot easier to avoid duplicates
        nums.sort()
        sol = []

        stack = deque()
        # format: (index, current subset)
        stack.append((0, []))
        # index is used to determine where in nums to start building the next subset

        while stack: 
            idx, curr = stack.pop()

            sol.append(curr)

            for i in range(idx, len(nums)): 
                # avoids duplicates by skipping duplicate terms
                if i > idx and nums[i] == nums[i - 1]: 
                    continue
                
                stack.append((i + 1, curr + [nums[i]]))
        
        return sol
