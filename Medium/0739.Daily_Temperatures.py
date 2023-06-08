class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # monotonic stack
        stack = []
        sol = [0] * len(temperatures)

        # general strategy: 
        #   if the current temp is higher than the top of stack
        #   pop all the cooler days and calculate how many days until hotter day
        for i in range(0, len(temperatures)): 
            # pop stack when current day is hotter than top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                curr = stack.pop()
                sol[curr] = i - curr
            
            # append indeces not temperatures
            stack.append(i)
        
        return sol
