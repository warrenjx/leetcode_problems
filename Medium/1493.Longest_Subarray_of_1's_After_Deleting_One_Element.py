class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # edge case: only 1 term
        if len(nums) == 1: 
            return 0
        
        # sets the rear pointer to calculate length of 1s
        end = 0
        if nums[0] == 0: 
            end = 1
        
        # used to hold pairs or singular counts of 1's separated by 1 zero
        groups = []
        # holds the current group
        curr = deque()

        idx = 1
        while idx < len(nums): 
            # only need to do something if 0 is found
            if nums[idx] == 0: 
                if idx - end <= 0: # this is true when a 2nd zero is found
                    groups.append(tuple(curr))
                    curr = deque()
                else: # if only 1 zero is found
                    # adds the current pair to groups
                    if len(curr) == 2: 
                        groups.append(tuple(curr))
                        # allows the second group to be formed 
                        curr.popleft()

                    # useful in cases like: 1 0 1 1 0 1 1 1 =? [(1,2),(2,3)]
                    curr.append(idx - end)
                # update rear pointer 
                end = idx + 1

            idx += 1

        # if last term is a 1, curr and group updating code wont trigger, so have it here too
        if nums[-1] == 1: 
            if len(curr) == 2: 
                groups.append(tuple(curr))
                curr.popleft()

            curr.append(idx - end)

        # will add last tuple, like if there is only 1 term
        groups.append(tuple(curr))

        # find the largest sum of groups
        sol = 0
        for group in groups: 
            sol = max(sum(group), sol)
        
        # edge case: if the array is all 1's
        if sol == len(nums): 
            sol -= 1
        
        return sol
