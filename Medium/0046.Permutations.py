class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # start the stack with the first terms
        stack = deque()
        for i in nums: 
            stack.append([i])
        
        # set incase of duplicates
        sol = set()

        # iteratively build possible solutions
        while stack: 
            curr = stack.pop()

            # add solution if it fits
            if len(curr) == len(nums): 
                sol.add(tuple(curr))
                continue
            
            # add new possible solutions
            for num in nums: 
                if num not in curr: 
                    stack.append(curr + [num])
        
        return sol
