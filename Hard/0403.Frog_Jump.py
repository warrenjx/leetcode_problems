class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        
        # translation from stone number to index
        S = {}
        for i in range(n): 
            S[stones[i]] = i

        # dp contains the jump distance at that stone from stone at index i
        #   i.e. dp[i][j] = k means: jumped from stones[i] to stones[j] with k jump distance
        dp = [[-1] * n for i in range(n)]

        # seeding the start
        dp[0][0] = 0

        # calculate jumps for every distance
        #   do not go to last term because you don't jump from there
        for i in range(n - 1): 
            # check each stone to see what are possible jumping points
            for j in range(n): 
                # if it has been jumped to
                if dp[i][j] != -1: 
                    jump = dp[i][j]

                    # cases in dfs solution
                    if (jump - 1) > 0 and stones[i] + (jump - 1) in S:
                        # reversing the relation explained in comment above dp initialization
                        #   i.e. dp[stone you jumped to][stone you jumped from] = jump distance
                        dp[S[stones[i] + (jump - 1)]][i] = jump - 1
                    if jump > 0 and stones[i] + jump in S: 
                        dp[S[stones[i] + jump]][i] = jump
                    if stones[i] + (jump + 1) in S: 
                        dp[S[stones[i] + (jump + 1)]][i] = jump + 1
        
        # if last row was reached then it was successful
        for i in range(n): 
            if dp[-1][i] != -1: 
                return True

        return False
