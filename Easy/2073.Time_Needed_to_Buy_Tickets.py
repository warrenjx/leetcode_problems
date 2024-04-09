class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        n = len(tickets)
        sol = 0

        # remove the common denominators
        base = min(tickets)
        for i in range(n): 
            tickets[i] -= base
        if tickets[k] == 0: 
            sol += (base * n) - (n - k - 1)
            return sol
        else: 
            sol += base * n

        # simulate the rest of the ticket buying
        i = 0
        while tickets[k] > 0: 
            if tickets[i] > 0: 
                tickets[i] -= 1
                sol += 1
            
            i += 1
            if i == n: 
                i = 0
        
        return sol
