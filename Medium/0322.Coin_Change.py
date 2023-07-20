class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp is array used to store the results of the sub problems
        #   sub problems are the amount of coins needed to reach n < amount
        dp = [-1] * (amount + 1)

        # 0 is always reachable by 0 coins
        dp[0] = 0

        for i in range(1, amount + 1): 
            min_coin = 10001 # placeholder
            for coin in coins: 
                if i == coin: # simplest case, only 1 coin needed reach sub problem
                    min_coin = 1
                    break
                elif i - coin > 0: # will need multiple coins
                    if dp[i - coin] == -1: # sub problem is not reachable
                        continue
                    else: # sub problem has its own amount of coins
                        min_coin = min(min_coin, dp[i - coin] + 1)
            
            if min_coin != 10001: # if a coin sum was actually found for the amount
                dp[i] = min_coin
                
        return dp[amount]
