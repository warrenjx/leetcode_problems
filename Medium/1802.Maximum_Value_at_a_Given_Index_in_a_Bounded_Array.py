class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        
        maxSum -= n # each term in array must be <= 1

        bot = 0
        top = maxSum

        # binary search a value between 0 and maxSum to find the best value
        while top >= bot: 
            mid = (top + bot) // 2

            # use formula to calculate the sum of the array based on BS value
            bot_sum = self.half_sum(index + 1, mid)
            top_sum = self.half_sum(n - index - 1, mid - 1)

            # get total sum and compare to maxSum
            if top_sum + bot_sum <= maxSum:     
                bot = mid + 1
            else: 
                top = mid - 1
        
        return bot


    # arithmetic progression formula
    def half_sum(self, n, end): 
        if n == 0: 
            return 0
        
        srt = max(end - n, 0)

        # formula is n * (n + 1) / 2
        sum_1 = (end * (1 + end)) // 2
        # calculate second sum incase it doesnt reach all the way to 0
        sum_2 = (srt * (1 + srt)) // 2

        return sum_1 - sum_2
