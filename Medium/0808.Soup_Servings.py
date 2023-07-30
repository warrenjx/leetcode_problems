class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        # recursion limiter: 
        # since on average A will get depleted faster than B, at large enough n just return 1
        if n >= 4800: 
            return 1.0

        # memoization dictionary for fast lookup
        memo = {}

        def dfs(a, b): 
            # base cases
            if a <= 0 and b <= 0: # both ran out of soup
                return 0.5
            elif a <= 0: # A ran out before B
                return 1.0
            elif b <= 0: # B ran outbefore A
                return 0.0
            
            # already calculated
            if (a, b) in memo: 
                return memo[(a, b)]

            # 4 cases of soup servings
            c_1 = dfs(a - 100, b - 0)
            c_2 = dfs(a - 75, b - 25)
            c_3 = dfs(a - 50, b - 50)
            c_4 = dfs(a - 25, b - 75)

            # memorize solution
            memo[(a, b)] = (c_1 + c_2 + c_3 + c_4) * 0.25

            return memo[(a, b)]
        
        return dfs(n, n)
