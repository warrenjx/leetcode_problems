class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)

        # holds how many candies each child gets
        chs = [1] * n

        # make sure every child has their left side satisfied
        for i in range(1, n): 
            if ratings[i] > ratings[i - 1]: 
                chs[i] = chs[i - 1] + 1

        # make sure every child has their right side satisfied
        for i in range(n - 2, -1, -1): 
            if ratings[i] > ratings[i + 1]: 
                chs[i] = max(chs[i], chs[i + 1] + 1)

        # 2 pass works because each child only cares about their neighbors
        return sum(chs)
