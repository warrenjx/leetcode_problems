class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1: 
            return 0

        max_profit = 0
        buy = prices[0]

        for sell in range(1, len(prices)):
            # check to see if current option has more profit
            max_profit = max(max_profit, prices[sell] - buy)
            # always set min to lowest you encounter
            buy = min(buy, prices[sell])

        return max_profit
