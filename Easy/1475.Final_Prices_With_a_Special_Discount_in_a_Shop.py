class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        stack = []

        # just daily temperatures again
        for i, val in enumerate(prices): 
            while stack and val <= prices[stack[-1]]: 
                curr = stack.pop()
                prices[curr] = prices[curr] - val

            stack.append(i)
        
        return prices