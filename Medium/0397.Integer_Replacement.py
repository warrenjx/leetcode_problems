class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        # dynamic programming stack implementation
        stack = deque()
        stack.append((n, 0))

        sol = n

        while stack: 
            curr_n, curr_ct = stack.pop()
            if curr_n == 1: 
                sol = min(curr_ct, sol)
                continue

            if (curr_n % 2) == 0: 
                stack.append((curr_n / 2, curr_ct + 1))
            elif (curr_n % 2) == 1: 
                stack.append((curr_n + 1, curr_ct + 1))
                stack.append((curr_n - 1, curr_ct + 1))
        
        return sol