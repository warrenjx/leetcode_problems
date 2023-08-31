class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        # ints is the maximum point in the garden that can be covered from sprinkler at i
        ints = [0] * (n + 1)
        # populate ints
        for i in range(n + 1): 
            # set it in the bounds of the garden for convenience
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            # multiple sprinklers can start from the same place, only care about farthest reaching (greedy)
            ints[start] = max(ints[start], end)

        sol = 0 # the amount of sprinklers on
        head = 0 # the current position in the garden
        while head < n: 
            tail = head # keep track of farthest you can sprinkle
            # greedily choose the next sprinkler to turn on
            for i in range(head + 1): # find the farthest you can sprinkle from the currently wetted garden
                head = max(head, ints[i])

            if head <= tail: # if you cant go further, it is impossible
                return -1
            
            # increase sprinkler count
            sol += 1

        return sol
