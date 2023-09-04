class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        sol = []

        stack = deque()
        # seed stack with starting digits
        for i in range(1, min(n, 9) + 1): 
            stack.append((i, [i]))

        while stack: 
            curr, path = stack.pop()

            if len(path) > k or curr > n: # invalid path termination conditions
                continue
            elif len(path) == k and curr == n: # valid solution conditions
                sol.append(path)

            # visit neighbors
            for i in range(path[-1] + 1, min(9, n) + 1): 
                stack.append((curr + i, path + [i]))
        
        return sol
