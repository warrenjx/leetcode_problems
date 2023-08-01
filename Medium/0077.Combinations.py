class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        sol = []

        stack = deque()

        # starting digits
        for i in range(n - k + 1): 
            stack.append(([i + 1], 1))
        
        sol = []
        # tail recursion converted to stack iteration
        while stack: 
            curr, l = stack.pop()

            # base case, curr is k long
            if l == k: 
                sol.append(curr)
                continue
            
            # visit neighbors, bound is up to max digit 
            for i in range(curr[-1] + 1, n + 1): 
                stack.append((curr + [i], l + 1))

        return sol
        
