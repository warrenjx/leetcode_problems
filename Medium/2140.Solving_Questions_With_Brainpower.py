class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)

        # each entry of dp holds the amount of points that can be attained if you answer the question at i
        # n + 1 to make algorithm simpler, dp[n] will always be 0
        dp = [0] * (n + 1)

        # fill in the array backwards to account for cooldowns better
        for i in range(n - 1, -1, -1): 
            pt, cd = questions[i]

            # comparing the cost of current points on top of the points at the question at cooldown
            # or just skipping current question, carrying over points from last question
            dp[i] = max(pt + dp[min(i + cd + 1, n)], dp[i + 1])
        
        # since array is filled in backwards, dp[0] is the solution
        return dp[0]
