class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        # keep track of how many losses each one has
        results = {}
        for win, los in matches: 
            # no need to keep track of wins
            if win not in results: 
                results[win] = 0

            if los not in results: 
                results[los] = 1
            else: 
                results[los] += 1

        winners = []
        one_loss = []

        # deposit the keys into their respective bins
        for key, val in results.items(): 
            if val == 0: 
                winners.append(key)
            elif val == 1: 
                one_loss.append(key)
        
        winners.sort()
        one_loss.sort()

        return [winners, one_loss]
