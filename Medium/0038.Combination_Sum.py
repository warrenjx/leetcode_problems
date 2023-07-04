class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = []

        # use stack to convert tail recursion to iteration
        stack = deque()
        # format: position in candidates, current sum, current path
        stack.append((0, 0, []))

        while stack: 
            start, curr_sum, curr_path = stack.pop()

            if curr_sum == target: 
                sol.append(curr_path)
            elif curr_sum > target: 
                continue
            
            # need to have lower limit to candidates to prevent duplicate sums in different orders
            for i in range(start, len(candidates)): 
                stack.append((i, curr_sum + candidates[i], curr_path + [candidates[i]]))
        
        return sol
