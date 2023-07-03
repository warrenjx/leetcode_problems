class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = set()
        # add base case, the empty set
        sol.add(())

        stack = deque()
        # add first case, the whole array
        # starting from top of array gets rid of issues with things being different order
        stack.append(nums)

        # iteratively add a case, then remove a term and re-add to stack
        while stack: 
            curr = stack.popleft()
            if not curr: 
                continue

            sol.add(tuple(curr))

            for i in range(len(curr)): 
                stack.append(curr[0:i] + curr[i + 1:len(curr)])
        
        return sol
