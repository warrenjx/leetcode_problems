class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # variable for convenience
        n = len(s)

        # dp array holds whether or not a position in s is reachable with words in wordDict
        dp = [False] * (n + 1)
        # dp[0] is the initial position
        dp[0] = True
        
        # iterate through entire dp array and filling in all positions that can be filled
        for i in range(n + 1): 
            # don't check any non-reachable positions
            if not dp[i]: 
                continue

            # check every word in dict
            for word in wordDict: 
                # variable dictates whether or not a word is fit
                passed = True

                for j in range(len(word)): 
                    if i + 1 + j > n: # if out of range in s
                        passed = False
                        break
                    elif word[j] != s[i + j]: # if characters don't match
                        passed = False
                        break

                # if word is in s, update the postion at the end of the word in s
                if passed: 
                    dp[i + len(word)] = True

        return dp[n]
