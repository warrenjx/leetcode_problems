class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [[False] * n for i in range(n)]
        # seed dp array with each character position
        for i in range(n): 
            dp[i][i] = True
        
        # each individual character is a palindrome, so start at n
        sol = n

        # parse through string backwards
        for start in range(n - 1, -1, -1): 
            # check if interval between start and end is palindrome
            for end in range(start + 1, n): 
                if s[start] == s[end]: 
                    # if it is a 2 character palidrome or based on previous iterations it is
                    if end - start == 1 or dp[start + 1][end - 1]: 
                        dp[start][end] = True

                        # all do is increment solution
                        sol += 1
        
        return sol
