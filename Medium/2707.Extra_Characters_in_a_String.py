class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        
        # dp holds the min amount of extra letters of s[0:i]
        dp = [0] * (n + 1)

        # fill in dp from 1 to n + 1 as 0 has default value of 0
        for i in range(1, n + 1): 
            # set dp[i] to worst case so far, another char to replace
            dp[i] = dp[i - 1] + 1

            # check for word matches
            for word in dictionary: 
                m = len(word)
                
                # word is too long
                if i - m < 0: 
                    continue
                
                # check if a word matches
                match = True
                for j in range(m): 
                    if s[i - m + j] != word[j]: 
                        match = False
                        break
                
                # retrieve dp value from where word matched to
                if match: 
                    dp[i] = min(dp[i], dp[i - m])

        return dp[n]
