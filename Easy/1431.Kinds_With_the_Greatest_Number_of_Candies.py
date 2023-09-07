class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)

        sol = [False] * n

        curr = max(candies)
        for i in range(n): 
            if candies[i] + extraCandies >= curr: 
                sol[i] = True

        return sol
