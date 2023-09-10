class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        sol = 1

        # basically just combinatorics
        for i in range(1, n + 1):  
            sol *= i
            sol *= (i * 2) - 1

        # for each increase in n, you have 2 more spots to fill, leading to 2^n spots. 
        # however, you cant just do (2 ^ n)! because there is some order that matters, the pickup must happen before the delivery
        # thus half of the options for every n you add are invalid, leading to the solution being: 
        # sol = (2 * n)! / (2 ^ n)
        
        # solution adjustment
        return int(sol % (1000000007))  
        
