class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        # create array used to keep track of iteration results
        dp = [[False] * n for i in range(n)]
        # seed each position of s in dp
        for i in range(n): 
            dp[i][i] = True

        # starting sol is last character of s
        sol = s[-1]
        # every singular character is a palindrome
        max_len = 1

        # iterate through s backwards
        for start in range(n - 1, -1, -1): 
            # find ending points
            for end in range(start + 1, n): 
                if s[start] == s[end]:
                    # if it is a 2 char palindrome, or characters inside of range are palindrome
                    if end - start == 1 or dp[start + 1][end - 1]: 
                        dp[start][end] = True
                        if end - start + 1 > max_len: 
                            max_len = end - start + 1
                            sol = s[start:end + 1]
        
        return sol
